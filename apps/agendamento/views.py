from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Agendamento
from .forms import AgendamentoForm
from apps.medico.models import Profissional, Servico
from apps.agenda_medico.models import AgendaMedica, Horario
from apps.paciente.models import Paciente

class CriarAgendamento(CreateView):
    model = Agendamento
    template_name = 'agendamento/modal_selecionar_paciente.html'
    form_class = AgendamentoForm
    pk_url_kwarg = 'horario_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pacientes'] = Paciente.objects.all()
        context['horario_pk'] = self.kwargs.get('horario_pk')
        return context

    def form_valid(self, form):
        horario_pk = self.kwargs.get('horario_pk')
        horario = Horario.objects.get(id=horario_pk)
        paciente_id = self.request.POST.get('paciente_id')
        paciente = Paciente.objects.get(id=paciente_id)
        form.instance.horario_selecionado = horario
        form.instance.paciente = paciente
        return super().form_valid(form)

    def get_success_url(self):
        horario_pk = self.kwargs.get('horario_pk')
        horario = Horario.objects.get(id=horario_pk)
        agenda_pk = horario.agenda_medica.pk
        print(agenda_pk)
        return reverse_lazy('agendamento:listar-agendamentos', kwargs={'agenda_pk': agenda_pk})

class ListarAgendamentos(ListView):
    model = Agendamento
    template_name = 'agendamento/agendamentos_solicitacoes.html'
    context_object_name = 'agendamentos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione a pk da agenda ao contexto
        context['agenda_pk'] = self.kwargs.get('agenda_pk')
        return context
