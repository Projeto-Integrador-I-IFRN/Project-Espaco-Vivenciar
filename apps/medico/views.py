from django.shortcuts import render

# Create your views here.
def GerenciarProfissionais(request):
    title = "Profissional"
    return render(request, 'medico/profissional.html', {'title': title})

def CadastrarProfissionais(request):
    title = "Cadastro de profissionais"
    context = {
        'title': title,
        'card': 'profissional',
        'info_user': True 
    }
    return render(request, 'medico/cadastrar_profissionais.html', context=context)

def NovoProfissional(request):
    title = "Novo profissional"
    return render(request, 'medico/novo_profissional.html', {'title': title})
