from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, View
from apps.medico.models import Profissional
from .models import AgendaMedica, Horario
from .forms import SelecionarAgendaForm
from django.views.generic.edit import FormView

class Home(ListView):
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
        servico_id = self.kwargs.get('servico_id')  # Obtenha o ID do serviço da URL
        profissional = Profissional.objects.get(pk=profissional_pk)
        context['profissional'] = profissional
        context['servico'] = profissional.servico_set.get(id=servico_id)  # Obtenha o serviço pelo ID
        context['agendas'] = profissional.agendamedica_set.filter(servico=context['servico'])

        for agenda in context['agendas']:
            listar_dias_semana(self, agenda= agenda)
        
        return context

def listar_dias_semana(self, agenda):

    dias_da_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
    dia_semana_numero = agenda.data.weekday()
    agenda.dia_semana_abreviado = dias_da_semana[dia_semana_numero]

    return agenda.dia_semana_abreviado

class ListarHorarios(ListView):
    model = Horario
    template_name = 'agenda_medico/listar_horarios.html'
    context_object_name = 'horarios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agenda_id = self.kwargs.get('agenda_id')
        agenda = AgendaMedica.objects.get(id=agenda_id)
        context['agenda'] = agenda
        
        listar_dias_semana(self, agenda)
    
        return context

    def get_queryset(self):
        agenda_id = self.kwargs.get('agenda_id')
        return Horario.objects.filter(agenda_medica__id=agenda_id)
