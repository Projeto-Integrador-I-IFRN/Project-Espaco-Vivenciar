from django.shortcuts import render
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import NovaAgenda
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy

# Create your views here.
def Home(request):
    title = "Home"
    return render(request, 'atendente/home.html', {'title': title} )

def GerenciarAgendas(request):
    title = "Gerenciar agendas"
    context = {
        'title': title,
        'card': 'agendamento',
        'data': True,
        'info_user': True,
        'info_user2': False,
        'horario': True,
        'horario2': True,
        'lista_servico': True,
        'button_solicitar': True,
        'button_whatsApp': True,
        'button_indeferido': False,
        'button_recusar': False,
        'button_aceitar': False,
        'edit': True,
        'edit2': False
    }
    return render(request, 'atendente/gerenciar_agenda.html', context=context)

def GerenciarProfissionais(request):
    title = "Profissional"
    return render(request, 'atendente/profissional.html', {'title': title})

def CadastrarProfissionais(request):
    title = "Cadastro de profissionais"
    context = {
        'title': title,
        'card': 'profissional',
        'info_user': True 
    }
    return render(request, 'atendente/cadastrar_profissionais.html', context=context)

def NovoProfissional(request):
    title = "Novo profissional"
    return render(request, 'atendente/novo_profissional.html', {'title': title})

def mostrar_modal_atendente(request):
    form = NovaAgenda()
    return render(request, 'atendente/modal2.html', {'form': form})

def AgendamentosSolicitacoes(request):
    title = "Solicitações"
    context = {
        'title': title,
        'card': 'agendamento',
        'data': True,
        'info_user': True,
        'info_user2': False,
        'horario': True,
        'horario2': True,
        'lista_servico': True,
        'button_solicitar': True,
        'button_whatsApp': True,
        'button_indeferido': False,
        'button_recusar': False,
        'button_aceitar': False,
        'button_detalhar': False,
        'count_agendados': False,
        'count_solicitacoes': False,
        'edit': True
    }
    return render(request, 'atendente/agendamentos_solicitacoes_consultas.html', context= context)


# CRUD PACIENTE
from apps.core.models import Paciente
from .forms import PacienteForm
class ListarPacientes(ListView):
    model = Paciente
    template_name = 'atendente/pacientes.html'
    context_object_name = 'pacientes'

class CriarPaciente(CreateView):
    template_name = 'atendente/criar-paciente.html'
    form_class = PacienteForm
    success_url = reverse_lazy('atendente:listar-pacientes')

class ExcluirPaciente(DeleteView):
    model = Paciente
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('atendente:listar-pacientes')

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class EditarPaciente(UpdateView):
    model = Paciente
    template_name = 'atendente/criar-paciente.html'
    form_class = PacienteForm
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        return reverse_lazy('atendente:listar-pacientes')