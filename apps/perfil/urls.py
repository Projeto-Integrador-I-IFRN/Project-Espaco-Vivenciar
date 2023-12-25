from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path("cadastro/", views.Cadastro, name="Cadastro"),
    path("login/", views.Login, name="Login"),
    path("perfil/", views.Perfil, name="Perfil"),
    path("agendamentos/", views.Agendamentos, name="Agendamentos"),
    path('home/selecionar-horario', views.mostrar_modal, name='Modal'),
    path("agendar/", views.Agendar, name="Agendar"),
]