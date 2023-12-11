from django.shortcuts import render
from apps.medico.models import Profissional
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
# from .forms import NovaAgenda
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy

# Create your views here.
class Home(ListView):
    model = Profissional
    template_name = 'atendente/home.html'
    context_object_name = 'profissionais'

def GerenciarAgendas(request):
    title = "Gerenciar agendas"
    context = {
        'title': title,
        'card': 'agendamento',
        'data': True,
        'info_user': True,
        'info_user2': False,
        'horario': True,
        'horario2': True,
        'lista_servico': True,
        'button_solicitar': True,
        'button_whatsApp': True,
        'button_indeferido': False,
        'button_recusar': False,
        'button_aceitar': False,
        'edit': True,
        'edit2': False
    }
    return render(request, 'atendente/gerenciar_agenda.html', context=context)

def mostrar_modal_atendente(request):
    form = NovaAgenda()
    return render(request, 'atendente/modal2.html', {'form': form})

def AgendamentosSolicitacoes(request):
    title = "Solicitações"
    context = {
        'title': title,
        'card': 'agendamento',
        'data': True,
        'info_user': True,
        'info_user2': False,
        'horario': True,
        'horario2': True,
        'lista_servico': True,
        'button_solicitar': True,
        'button_whatsApp': True,
        'button_indeferido': False,
        'button_recusar': False,
        'button_aceitar': False,
        'button_detalhar': False,
        'count_agendados': False,
        'count_solicitacoes': False,
        'edit': True
    }
    return render(request, 'atendente/agendamentos_solicitacoes_consultas.html', context= context)
