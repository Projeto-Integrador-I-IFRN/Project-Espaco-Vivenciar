from django.shortcuts import render
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import NovaAgenda

# Create your views here.
def Home(request):
    return render(request, 'atendente/home.html')

def Gerenciar(request):
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
        'edit': True
    }
    return render(request, 'atendente/cadastrar_agenda.html', context=context)

def GerenciarProfissionais(request):
    return render(request, 'atendente/gerenciar_profissionais.html')

def mostrar_modal_atendente(request):
    form = NovaAgenda()
    return render(request, 'atendente/modal2.html', {'form': form})