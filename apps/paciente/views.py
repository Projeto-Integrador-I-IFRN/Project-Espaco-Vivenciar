from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from apps.paciente.models import Paciente
from django.db.models import Q
from .forms import PacienteForm
from django.urls import reverse_lazy
import re

class ListarPacientes(ListView):
    model = Paciente
    template_name = 'paciente/pacientes.html'
    context_object_name = 'pacientes'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Paciente.objects.all()
        if query:
            object_list = object_list.filter(Q(nome_paciente__icontains=query)| Q(cpf_paciente__icontains=query))
            
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Formata o CPF de cada paciente na lista
        for paciente in context['pacientes']:
            paciente.cpf_formatado = formatar_cpf(paciente.cpf_paciente)

        return context

def formatar_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf_numerico = re.sub('[^0-9]', '', str(cpf))

    # Formata o CPF
    cpf_formatado = '{}.{}.{}-{}'.format(cpf_numerico[:3], cpf_numerico[3:6], cpf_numerico[6:9], cpf_numerico[9:])
    
    return cpf_formatado

class CriarPaciente(CreateView):
    template_name = 'paciente/criar-paciente.html'
    form_class = PacienteForm
    success_url = reverse_lazy('paciente:listar-pacientes')

class ExcluirPaciente(DeleteView):
    model = Paciente
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('paciente:listar-pacientes')

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class EditarPaciente(UpdateView):
    model = Paciente
    template_name = 'paciente/criar-paciente.html'
    form_class = PacienteForm
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        return reverse_lazy('paciente:listar-pacientes')