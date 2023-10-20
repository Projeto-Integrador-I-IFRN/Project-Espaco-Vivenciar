from django.shortcuts import render

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