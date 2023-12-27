from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView, FormView
from .forms import UserProfileMultiForm, PerfilUserForm
from apps.paciente.models import Paciente
from apps.medico.models import Profissional
from django.db.models import Q
from .forms import PacienteForm
from apps.agenda_medico.forms import SelecionarAgendaForm
from apps.agenda_medico.models import AgendaMedica, Horario
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import re
from apps.perfil.views import CreateUserAndPacienteMixin


class Home(ListView):
    model = Profissional
    template_name = 'paciente/home.html'
    context_object_name = 'profissionais'

class SelecionarAgendaView(FormView):
    template_name = 'paciente/modal_selecionar_agenda.html'
    form_class = SelecionarAgendaForm
    pk_url_kwarg = 'profissional_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profissional_pk = self.kwargs.get('profissional_pk')
        profissional = Profissional.objects.get(pk=profissional_pk)
        context['profissional'] = profissional
        context['servicos'] = profissional.servico_set.all()
        return context

    def form_valid(self, form):
        profissional_pk = self.kwargs.get('profissional_pk')
        profissional = Profissional.objects.get(pk=profissional_pk)
        servico = form.cleaned_data['servico']
        
        self.cleaned_data = {'servico': servico}

        return super().form_valid(form)

    def get_success_url(self):
        profissional_pk = self.kwargs.get('profissional_pk')
        profissional = Profissional.objects.get(pk=profissional_pk)
        servico = self.cleaned_data['servico']

        return reverse_lazy('paciente:listar-agendas', kwargs={'profissional_pk': profissional_pk, 'servico_id': servico.id})

    def get_form_kwargs(self):
        kwarg = super().get_form_kwargs()
        profissional_pk = self.kwargs.get('profissional_pk')
        profissional = Profissional.objects.get(pk=profissional_pk)
        kwarg['profissional'] = profissional
        return kwarg


class ListarAgenda(ListView):
    model = AgendaMedica
    template_name = 'paciente/listar-agendas.html'
    context_object_name = 'agendas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profissional_pk = self.kwargs.get('profissional_pk')
        servico_id = self.kwargs.get('servico_id')
        profissional = Profissional.objects.get(pk=profissional_pk)
        context['profissional'] = profissional
        context['servico'] = profissional.servico_set.get(id=servico_id)
        context['agendas'] = profissional.agendamedica_set.filter(servico=context['servico'])
        context['servico_id'] = servico_id
        context['profissional_pk'] = profissional_pk

        for agenda in context['agendas']:
            agenda.dia_semana_abreviado = listar_dias_semana(agenda)

        return context
        
def listar_dias_semana(agenda):
    dias_da_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
    dia_semana_numero = agenda.data.weekday()
    return dias_da_semana[dia_semana_numero]

class ListarHorarios(ListView):
    model = Horario
    template_name = 'paciente/listar-horarios-atendimento.html'
    context_object_name = 'horarios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agenda_id = self.kwargs.get('agenda_id')
        agenda = AgendaMedica.objects.get(id=agenda_id)
        context['agenda'] = agenda
        context['dia_semana_abreviado'] = listar_dias_semana(agenda)
        return context

    def get_queryset(self):
        agenda_id = self.kwargs.get('agenda_id')
        return Horario.objects.filter(agenda_medica__id=agenda_id)
    
class ListarPacientes(ListView):
    model = Paciente
    template_name = 'paciente/pacientes.html'
    context_object_name = 'pacientes'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('search')

        object_list = Paciente.objects.all()
        if query:
            object_list = object_list.filter(Q(nome_paciente__icontains=query) | Q(cpf_paciente__icontains=query))
            
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Formata o CPF de cada paciente na lista
        for paciente in context['pacientes']:
            paciente.cpf_formatado = formatar_cpf(paciente.cpf_paciente)

        return context

def formatar_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf_numerico = re.sub('[^0-9]', '', str(cpf))

    # Formata o CPF
    cpf_formatado = '{}.{}.{}-{}'.format(cpf_numerico[:3], cpf_numerico[3:6], cpf_numerico[6:9], cpf_numerico[9:])
    
    return cpf_formatado

class CriarPaciente(LoginRequiredMixin, CreateUserAndPacienteMixin, CreateView):
    template_name = 'paciente/criar-paciente.html'
    form_class = UserProfileMultiForm
    success_url = reverse_lazy('paciente:listar-pacientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paciente_form'] = PacienteForm()
        return context

    def get_user(self, user):
        return self.request.user

class ExcluirPaciente(DeleteView):
    model = Paciente
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('paciente:listar-pacientes')

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class EditarPaciente(UpdateView):
    model = Paciente
    template_name = 'paciente/criar-paciente.html'
    form_class = PacienteForm
    pk_url_kwarg = 'id'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        if 'instance' not in kwargs:
            kwargs['instance'] = self.get_object()

        # Certifique-se de que o campo de data de nascimento é convertido para string antes de passá-lo para o formulário
        if 'data_nascimento' in kwargs['instance'].__dict__:
            kwargs['instance'].data_nascimento = str(kwargs['instance'].data_nascimento)

        return kwargs

    def get_success_url(self):
        return reverse_lazy('paciente:listar-pacientes')

