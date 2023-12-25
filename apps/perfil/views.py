from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import SolicitarConsulta
from django.views.generic import View, TemplateView, CreateView
from .forms import PerfilUserForm
from .models import PerfilUser
from apps.paciente.forms import PacienteForm
# Create your views here

class RegisterPacienteView(CreateView):
    model = PerfilUser
    form_class = PerfilUserForm
    template_name = 'perfil/cadastro.html'
    success_url = reverse_lazy('perfil:Login')

    def form_valid(self, form):
        # Create the Paciente form based on POST data
        paciente_form = PacienteForm(self.request.POST)

        # Check if both forms are valid
        if form.is_valid() and paciente_form.is_valid():
            # Create an instance of PerfilUser (user)
            user = form.save()

            # Create an instance of Paciente associated with PerfilUser
            paciente = paciente_form.save(commit=False)
            paciente.user = user
            paciente.save()
            print('paciente cadastrado')
            # Authenticate the newly created user
            login(self.request, user)

            # Redirect to the success URL
            return redirect('perfil:Cadastro')

        # If one of the forms is not valid, return to the page with errors
        else:
            # Pass both forms to the template context for error display
            return self.render_to_response(self.get_context_data(form=form, paciente_form=paciente_form))

    def form_invalid(self, form):
        # If the PerfilUser form is invalid, call the form_invalid method of the parent class
        response = super().form_invalid(form)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the PacienteForm instance to the template context
        context['paciente_form'] = kwargs.get('paciente_form', PacienteForm())
        return context

    
def Login(request):
    return render(request, 'perfil/login.html')

def Home(request):
    return render(request, 'perfil/home.html')

def Perfil(request):
    return render(request, 'perfil/perfil.html')

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

def mostrar_modal(request):
    form = SolicitarConsulta()
    return render(request, 'perfil/modal.html', {'form': form})
def Agendar(request):
    context = {
        'block': 'main_agendar', 
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
        'edit': True  
    }
    return render(request, 'perfil/agendar.html', context)
