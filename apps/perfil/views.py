from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic import CreateView, TemplateView, ListView
from .forms import UserProfileMultiForm
from apps.paciente.forms import PacienteForm
from apps.paciente.models import Paciente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from apps.agendamento.models import Agendamento
from django.shortcuts import get_object_or_404

class CreateUserAndPacienteMixin:
    def form_valid(self, form):
        user = form['perfiluser'].save(commit=False)
        user.username = form['perfiluser'].cleaned_data.get('email')
        user.save()
        paciente = form['pacienteuser'].save(commit=False)
        paciente.user = self.get_user(user)
        paciente.save()
        return super().form_valid(form)

    def get_user(self, user):
        return user
    
class RegisterPacienteView(CreateUserAndPacienteMixin, CreateView):
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

    def get_object(self, queryset=None):
        # Certifique-se de que o usuário autenticado seja o dono do perfil
        paciente = get_object_or_404(Paciente, user=self.request.user)
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
        paciente = Paciente.objects.filter(user__id=self.request.user.id)
        print(paciente)
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

class ListarAgendamentos(LoginRequiredMixin, ListView):
    template_name = 'perfil/listar_agendamentos.html'
    model = Agendamento
    context_object_name = 'agendamentos'

    def get_queryset(self):
        # Recupera o paciente logado
        paciente = Paciente.objects.filter(user__id=self.request.user.id).first()

        # Filtra os agendamentos para o paciente logado
        queryset = Agendamento.objects.filter(paciente=paciente)

        # Adicione qualquer lógica adicional de filtragem aqui, se necessário

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adiciona o atributo 'dia_semana_abreviado' e 'agenda' a cada objeto de Agendamento no contexto
        for agendamento in context['agendamentos']:
            agendamento.agenda = agendamento.agenda_medica
            agendamento.agenda.dia_da_semana = listar_dias_semana(agendamento)

        return context

def listar_dias_semana(agendamento):
    dias_da_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
    dia_semana_numero = agendamento.agenda_medica.data.weekday()
    return dias_da_semana[dia_semana_numero]
