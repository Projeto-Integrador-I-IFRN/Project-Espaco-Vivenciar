from django.shortcuts import render, redirect

# Create your views here.

def Cadastro(request):
    return render(request, 'perfil/cadastro.html')
    

def Perfil(request):
    return render(request, 'perfil/perfil.html')
