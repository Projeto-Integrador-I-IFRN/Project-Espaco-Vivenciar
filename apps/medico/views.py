# views.py

from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from apps.core.models import Profissional, Servico
from .forms import ServicoForm

def CadastrarProfissionais(request):
    title = "Cadastro de profissionais"
    context = {
        'title': title,
        'card': 'profissional',
        'info_user': True 
    }
    return render(request, 'medico/novo_profissional.html', context=context)

class ListarProfissionais(ListView):
    model = Profissional
    template_name = 'medico/listar_profissionais.html'
    context_object_name = 'profissionais'

# class CriarProfissional(CreateView):
#     template_name = 'medico/novo_profissional.html'
#     # Adicione o model e o form_class conforme necessário

class CriarServico(CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'medico/modal_add_service.html'
    success_url = reverse_lazy('medico:listar-profissionais')
