from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'perfil'

urlpatterns = [
    path("cadastro/", views.RegisterPacienteView.as_view(), name="Cadastro"),
    path("login/", views.Login.as_view(), name="Login"),
    path("logout/", LogoutView.as_view(), name="Logout"),
    path("home/", views.HomeView.as_view(), name="Home"),
    path("perfil/", views.Perfil, name="Perfil"),
    path("agendamentos/", views.Agendamentos, name="Agendamentos"),
    path('home/selecionar-horario', views.mostrar_modal, name='Modal'),
    path("agendar/", views.Agendar, name="Agendar"),
]