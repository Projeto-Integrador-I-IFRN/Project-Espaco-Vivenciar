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
    return render(request, 'perfil/agendamentos.html')
