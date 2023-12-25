from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, View, CreateView
from .models import Agendamento, Solicitacao
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

class ListarAgendamentosSolicitacoes(ListView):
    template_name = 'agendamento/agendamentos_solicitacoes.html'
    model = Agendamento

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipo_modelo = self.request.GET.get('tipo_modelo', 'agendamento')

        agenda_medica_id = self.kwargs.get('agenda_pk')  # Correct the parameter name

        if tipo_modelo == 'agendamento':
            queryset = Agendamento.objects.filter(horario_selecionado__agenda_medica__id=agenda_medica_id)
        elif tipo_modelo == 'solicitacao':
            queryset = Solicitacao.objects.filter(horario_selecionado__agenda_medica__id=agenda_medica_id)
        else:
            queryset = Agendamento.objects.filter(horario_selecionado__agenda_medica__id=agenda_medica_id)

        context['itens'] = queryset.select_related('horario_selecionado__agenda_medica').all()
        context['tipo_modelo'] = tipo_modelo

        if queryset.exists():
            # Retrieve and add the 'servico' to the context
            agenda_medica = queryset.first().horario_selecionado.agenda_medica
            context['itens'] = queryset.select_related('horario_selecionado__agenda_medica').all()
            context['servico'] = agenda_medica.servico

            # Pass the list of days of the week to the context
            context['dias_da_semana'] = self.listar_dias_semana(agenda_medica)

            # Add a flag indicating the type of the item
            context['is_agendamento'] = isinstance(queryset.first(), Agendamento)

            # Add counts to the context
            context['count_agendamentos'] = Agendamento.objects.filter(horario_selecionado__agenda_medica__id=agenda_medica_id).count()
            context['count_solicitacoes'] = Solicitacao.objects.filter(horario_selecionado__agenda_medica__id=agenda_medica_id).count()

        return context

    def listar_dias_semana(self, agenda):
        dias_da_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
        dia_semana_numero = agenda.data.weekday()
        return dias_da_semana[dia_semana_numero]

