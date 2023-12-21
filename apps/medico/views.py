# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

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
        return reverse('medico:detalhe-profissional', kwargs={'profissional_pk': self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.get_success_url())


class ExcluirProfissional(DeleteView):
    model = Profissional
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('medico:listar-profissionais')

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)


class EditarProfissional(UpdateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'medico/novo_profissional.html'
    pk_url_kwarg = 'profissional_pk'

    def get_success_url(self):
        # Após salvar o serviço, redirecione de volta para a página de detalhes do profissional
        return reverse('medico:detalhe-profissional', kwargs={'profissional_pk': self.object.pk})

class CriarServico(CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'medico/modal_add_service.html'
    success_url = reverse_lazy('medico:detalhe-profissional')  # Mudado para detalhe-profissional

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profissional_pk = self.kwargs.get('profissional_pk')
        profissional = Profissional.objects.get(pk=profissional_pk)
        context['profissional_pk'] = profissional_pk
        context['profissional'] = profissional
        return context
    
    def form_valid(self, form):
        # Antes de salvar o formulário, defina o profissional com base no contexto
        form.instance.profissional = self.get_context_data()['profissional']
        response = super().form_valid(form)
        return redirect(self.get_success_url())

    def get_success_url(self):
        # Após salvar o serviço, redirecione de volta para a página de detalhes do profissional
        return reverse('medico:detalhe-profissional', kwargs={'profissional_pk': self.get_context_data()['profissional_pk']})

class ListarServico(ListView):
    model = Servico
    template_name = 'medico/cadastrar-servicos.html'
    context_object_name = 'servicos'  

class DetalharProfissional(DetailView):
    model = Profissional
    template_name = 'medico/adicionar_servicos.html'
    context_object_name = 'profissional'
    pk_url_kwarg = 'profissional_pk'
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profissional = context[self.context_object_name]
        context['servicos'] = profissional.servico_set.all()
        return context
    
class ExcluirServico(DeleteView):
    model = Servico
    success_url = reverse_lazy('medico:detalhe-profissional')
    pk_url_kwarg = 'servico_pk'

    def get_success_url(self):
        profissional_pk = self.kwargs['profissional_pk']
        return reverse_lazy('medico:detalhe-profissional', kwargs={'profissional_pk': profissional_pk})

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
class EditarServico(UpdateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'medico/modal_edit_service.html'
    context_object_name = 'servico'
    pk_url_kwarg = 'servico_pk'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profissional_pk = self.kwargs.get('profissional_pk')
        profissional = Profissional.objects.get(pk = profissional_pk)
        context['profissional_pk'] = profissional_pk
        context['profissional'] = profissional
        return context

    def get_success_url(self):
        profissional_pk = self.kwargs['profissional_pk']
        return reverse_lazy('medico:detalhe-profissional', kwargs={'profissional_pk': profissional_pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.get_success_url())