from django.urls import path
from .views import ListarAgendamentos, DetalhesPaciente, HomeView, RegisterPacienteView, EditarPaciente, Login
from django.contrib.auth.views import LogoutView

app_name = 'perfil'

urlpatterns = [
    path("cadastro/", RegisterPacienteView.as_view(), name="Cadastro"),
    path("login/", Login.as_view(), name="Login"),
    path("logout/", LogoutView.as_view(), name="Logout"),
    path("home/", HomeView.as_view(), name="Home"),
    path('listar-agendamentos/', ListarAgendamentos.as_view(), name='listar-agendamentos'),
    path('perfil/detalhes/', DetalhesPaciente.as_view(), name='detalhes-paciente'),
    path('perfil/editar/', EditarPaciente.as_view(), name='editar-paciente'),
]
