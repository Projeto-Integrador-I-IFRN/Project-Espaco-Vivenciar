from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import RedirectView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import ListView, View, CreateView, UpdateView, DetailView
from .forms import SolicitarConsulta
from django.views.generic import CreateView, TemplateView
from .forms import UserProfileMultiForm, PerfilUserForm
from apps.paciente.forms import PacienteForm
from apps.paciente.models import Paciente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


class RegisterPacienteView(CreateView):
    model = Paciente
    form_class = UserProfileMultiForm
    template_name = 'perfil/cadastro.html'
    success_url = reverse_lazy('perfil:Login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paciente_form'] = PacienteForm() 
        return context

    def form_valid(self, form):
        user = form['perfiluser'].save()
        user.username = form['perfiluser'].cleaned_data.get('email')
        user.save()
        paciente = form['pacienteuser'].save(commit=False)
        paciente.user = user
        paciente.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        paciente_form = PacienteForm(self.request.POST)
        return self.render_to_response(self.get_context_data(form=form, paciente_form=paciente_form))

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

