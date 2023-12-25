from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, View, CreateView
from .forms import SolicitarConsulta
from apps.medico.models import Profissional

# Create your views here.

def Cadastro(request):
    return render(request, 'perfil/cadastro.html')
    
def Login(request):
    return render(request, 'perfil/login.html')


def Perfil(request):
    return render(request, 'perfil/perfil.html')

def Agendamentos(request):
    context = {
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
    return render(request, 'perfil/agendamentos.html', context=context)

from django.shortcuts import render

def mostrar_modal(request):
    form = SolicitarConsulta()
    return render(request, 'perfil/modal.html', {'form': form})
def Agendar(request):
    context = {
        'block': 'main_agendar', 
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
        'edit': True  
    }
    return render(request, 'perfil/agendar.html', context)
