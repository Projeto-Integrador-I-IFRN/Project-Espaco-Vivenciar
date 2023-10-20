from django.shortcuts import render, redirect

# Create your views here.

def Cadastro(request):
    return render(request, 'perfil/cadastro.html')
    
def Login(request):
    return render(request, 'perfil/login.html')

def Home(request):
    return render(request, 'perfil/home.html')

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
        'edit': True
    }
    return render(request, 'perfil/agendamentos.html', context=context)

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