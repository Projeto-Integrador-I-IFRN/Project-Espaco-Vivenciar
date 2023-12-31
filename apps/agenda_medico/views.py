from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, View
from apps.medico.models import Profissional, Servico
from .models import AgendaMedica, Horario
from .forms import SelecionarAgendaForm, AgendaMedicaForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.agendamento.models import Agendamento, Solicitacao

class Home(LoginRequiredMixin, ListView):
    model = Profissional
    template_name = 'agenda_medico/home.html'
    context_object_name = 'profissionais'

class SelecionarAgendaView(FormView):
    template_name = 'agenda_medico/modal_escolher_agenda.html'
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

        return reverse_lazy('agenda_medico:listar-agenda', kwargs={'profissional_pk': profissional_pk, 'servico_id': servico.id})

    def get_form_kwargs(self):
        kwarg = super().get_form_kwargs()
        profissional_pk = self.kwargs.get('profissional_pk')
        profissional = Profissional.objects.get(pk=profissional_pk)
        kwarg['profissional'] = profissional
        return kwarg


class ListarAgenda(ListView):
    model = AgendaMedica
    template_name = 'agenda_medico/gerenciar_agenda.html'
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

            # Add the counts to each agenda
            agenda.agendamentos_count = Agendamento.objects.filter(horario_selecionado__agenda_medica=agenda).count()
            agenda.solicitacoes_count = Solicitacao.objects.filter(horario_selecionado__agenda_medica=agenda).count()

        return context

def listar_dias_semana(agenda):
    dias_da_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
    dia_semana_numero = agenda.data.weekday()
    return dias_da_semana[dia_semana_numero]

class CriarAgendaView(CreateView):
    model = AgendaMedica
    form_class = AgendaMedicaForm
    template_name = 'agenda_medico/modal_criar_agenda.html'
    success_url = reverse_lazy('agenda_medico:listar-agenda')

    def form_valid(self, form):
        profissional_pk = self.kwargs.get('profissional_pk')
        servico_id = self.kwargs.get('servico_id')

        servico = Servico.objects.get(id=servico_id)
        profissional = Profissional.objects.get(pk=profissional_pk)
    
        form.instance.profissional = profissional
        form.instance.servico = servico

        agenda_medica_instance = form.save()

        # Chama o método para gerar os horários da agenda
        agenda_medica_instance.gerar_horarios_atendimento()

        return super().form_valid(form)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profissional_pk = self.kwargs.get('profissional_pk')
        servico_id = self.kwargs.get('servico_id')

        # Certifique-se de que está passando o objeto Servico corretamente para o contexto
        servico = Servico.objects.get(id=servico_id)
        profissional = Profissional.objects.get(pk=profissional_pk)

        context['profissional_pk'] = profissional_pk
        context['servico_id'] = servico_id
        context['servico'] = servico
        context['profissional'] = profissional

        return context
    
    def get_success_url(self):
        profissional_pk = self.kwargs.get('profissional_pk')
        servico_id = self.kwargs.get('servico_id')
        return reverse_lazy('agenda_medico:listar-agenda', kwargs={'profissional_pk': profissional_pk, 'servico_id': servico_id})
    
class ExcluirAgenda(DeleteView):
    model = AgendaMedica
    template_name = 'agenda_medico/excluir_agenda.html'  
    success_url = reverse_lazy('agenda_medico:listar-agenda')
    pk_url_kwarg = 'agenda_pk'

    def get_success_url(self):
        profissional_pk = self.object.profissional.pk
        servico_id = self.object.servico.id
        return reverse_lazy('agenda_medico:listar-agenda', kwargs={'profissional_pk': profissional_pk, 'servico_id': servico_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        agenda = self.object
        context['profissional_pk'] = agenda.profissional.pk
        context['servico_id'] = agenda.servico.id
        context['agenda_pk'] = agenda.pk
        print(agenda.pk)
       
        return context
    

class ListarHorarios(ListView):
    model = Horario
    template_name = 'agenda_medico/listar_horarios.html'
    context_object_name = 'horarios'
    paginate_by = 4

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


class ExcluirHorario(DeleteView):
    model = Horario
    template_name = 'agenda_medico/excluir_horario.html' 
    pk_url_kwarg = 'horario_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agenda_pk = self.kwargs.get('agenda_pk')
        horario_pk = self.kwargs.get('horario_pk')
        agenda = AgendaMedica.objects.get(id=agenda_pk)
        context['agenda'] = agenda
        context['agenda_pk'] = agenda_pk
        return context
    
    def get_success_url(self):
        agenda_pk = self.kwargs.get('agenda_pk')
        return reverse_lazy('agenda_medico:listar-horarios', kwargs={'agenda_id': agenda_pk})