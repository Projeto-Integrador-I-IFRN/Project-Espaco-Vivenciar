from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from apps.core.models import Paciente
from .forms import PacienteForm
from django.urls import reverse_lazy

class ListarPacientes(ListView):
    model = Paciente
    template_name = 'paciente/pacientes.html'
    context_object_name = 'pacientes'

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