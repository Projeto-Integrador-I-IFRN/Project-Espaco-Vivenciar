from django.shortcuts import render
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import NovaAgenda

# Create your views here.
def Home(request):
    title = "Home"
    return render(request, 'atendente/home.html', {'title': title} )

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

def GerenciarProfissionais(request):
    title = "Profissional"
    return render(request, 'atendente/profissional.html', {'title': title})

def GerenciarPacientes(request):
    title = "Paciente"
    return render(request, 'atendente/pacientes.html', {'title': title})

def CadastrarProfissionais(request):
    title = "Cadastro de profissionais"
    context = {
        'title': title,
        'card': 'profissional',
        'info_user': True 
    }
    return render(request, 'atendente/cadastrar_profissionais.html', context=context)

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
    return render(request, 'atendente/agendamentos_solicitacoes_consultas.html', context=context)