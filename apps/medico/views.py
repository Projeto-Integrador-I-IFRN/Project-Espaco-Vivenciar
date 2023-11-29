from django.shortcuts import render
from django.views.generic import  CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from apps.core.models import Profissional

# Create your views here.
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

class ListarProfissionais(ListView):
    model = Profissional
    template_name = 'medico/listar_profissionais.html'
    context_object_name = 'profissionais'


