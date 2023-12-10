# views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from django.urls import reverse_lazy
from apps.medico.models import Profissional, Servico
from .forms import ServicoForm, ProfissionalForm
from django.contrib import messages

class ListarProfissionais(ListView):
    model = Profissional
    template_name = 'medico/listar_profissionais.html'
    context_object_name = 'profissionais'

class CriarProfissional(CreateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'medico/novo_profissional.html'
    success_url = reverse_lazy('medico:listar-profissionais')

    def get_success_url(self):
        print('---------------------------------------------------------------------------------\n')
        print(self.object.id)
        return reverse('medico:criar-servico', kwargs={'profissional_pk': self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.get_success_url())


class ExcluirProfissional(DeleteView):
    model = Profissional
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('medico:listar-profissionais')

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class CriarServico(CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'medico/modal_add_service.html'
    success_url = reverse_lazy('medico:listar-profissionais')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profissional_pk = self.kwargs.get('profissional_pk')
        context['profissional_pk'] = profissional_pk
        return context


class ListarServico(ListView):
    model = Servico
    template_name = 'medico/cadastrar-servicos.html'
    context_object_name = 'servicos'  # Alterado para 'servicos'
   