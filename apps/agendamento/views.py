from django.http import request
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, View
from apps.medico.models import Profissional, Servico
from apps.agenda_medico.models import AgendaMedica, Horario
from apps.paciente.models import Paciente
from .models import Agendamento
from .forms import AgendamentoForm

class CriarAgendamento(CreateView):
    model = Agendamento
    template_name = 'agenda_medico/modal_selecionar_paciente.html'
    success_url = reverse_lazy('agenda_medico:listar-agenda')
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