from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, View, CreateView
from .models import Agendamento, Solicitacao
from .forms import AgendamentoForm
from apps.medico.models import Profissional, Servico
from apps.agenda_medico.models import AgendaMedica, Horario
from apps.paciente.models import Paciente
from .utils import obter_dia_semana_por_agenda_id

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

class ListarAgendamentosSolicitacoes(ListView):
    template_name = 'agendamento/agendamentos_solicitacoes.html'
    model = Agendamento

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipo_modelo = self.request.GET.get('tipo_modelo', 'agendamento')

        if tipo_modelo == 'agendamento':
            queryset = Agendamento.objects.all()
        elif tipo_modelo == 'solicitacao':
            queryset = Solicitacao.objects.all()
        else:
            queryset = Agendamento.objects.all()

        # Assuming horario_selecionado has agenda_medica field
        context['itens'] = queryset.select_related('horario_selecionado__agenda_medica').all()

        context['tipo_modelo'] = tipo_modelo
        return context