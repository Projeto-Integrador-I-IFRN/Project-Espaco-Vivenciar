from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic import CreateView, TemplateView
from .forms import UserProfileMultiForm
from apps.paciente.forms import PacienteForm
from apps.paciente.models import Paciente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404


class ListarAgendamentos(LoginRequiredMixin, ListView):
    template_name = 'perfil/listar_agendamentos.html'
    model = Agendamento
    context_object_name = 'agendamentos'
    paginate_by = 5

    def get_queryset(self):
        # Recupera o paciente logado
        paciente = get_object_or_404(Paciente, id=1)

        # Filtra os agendamentos para o paciente logado
        queryset = Agendamento.objects.filter(paciente=paciente)

        # Adicione qualquer lógica adicional de filtragem aqui, se necessário

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicione qualquer informação adicional ao contexto, se necessário

        return context

class RegisterPacienteView(CreateView):
    model = Paciente
    form_class = UserProfileMultiForm
    template_name = 'perfil/cadastro.html'
    success_url = reverse_lazy('perfil:Login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paciente_form'] = PacienteForm()
        return context

class CustomUserRedirectView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return reverse("agenda_medico:Home")
            else:
                print('aaaaa')
                return reverse("paciente:Home")
        else:
            print('test')
            return reverse("perfil:Login")
    
class Login(LoginView):
    template_name = 'perfil/login.html'

    def get_default_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return reverse("agenda_medico:Home")
            else:
                return reverse("paciente:Home")
        else:
            print('test')
            return reverse("perfil:Login")


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'paciente/home.html'

def Perfil(request):
    return render(request, 'perfil/perfil.html')

class EditarPaciente(LoginRequiredMixin, UpdateView):
    model = Paciente
    template_name = 'perfil/perfil.html'
    form_class = PacienteForm
    pk_url_kwarg = 'paciente_id'

    def get_object(self, queryset=None):
        # Certifique-se de que o usuário autenticado seja o dono do perfil
        paciente = Paciente.objects.get(id=1)
        return paciente

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if 'data_nascimento' in kwargs['instance'].__dict__:
            kwargs['instance'].data_nascimento = str(kwargs['instance'].data_nascimento)
        return kwargs

    def get_success_url(self):
        return reverse("paciente:Home")

class DetalhesPaciente(DetailView):
    model = Paciente
    template_name = 'perfil/detalhes_paciente.html'  # Certifique-se de criar este arquivo HTML

    def get_object(self, queryset=None):
        # Certifique-se de que o usuário autenticado seja o dono do perfil
        paciente = Paciente.objects.get(id=1)  # Modifique isso conforme necessário para obter o paciente certo
        return paciente

def Agendamentos(request):
    context = {
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
    return render(request, 'perfil/agendamentos.html', context=context)

from django.shortcuts import render

