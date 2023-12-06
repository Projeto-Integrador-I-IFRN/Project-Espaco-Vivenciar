# views.py

from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from apps.core.models import Profissional, Servico
from .forms import ServicoForm, ProfissionalForm


class ListarProfissionais(ListView):
    model = Profissional
    template_name = 'medico/listar_profissionais.html'
    context_object_name = 'profissionais'

class CriarProfissional(CreateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'medico/novo_profissional.html'
    success_url = reverse_lazy('medico:listar-profissionais')

class CriarServico(CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'medico/modal_add_service.html'
    success_url = reverse_lazy('medico:listar-servico')

class ListarServico(ListView):
    model = Servico
    template_name = 'medico/novo_profissional.html'
    context_object_name = 'servicos'  # Alterado para 'servicos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()  # Adicionado para fornecer a lista de serviços
        return context