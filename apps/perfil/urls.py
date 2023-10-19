from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path("cadastro/", views.Cadastro, name="Cadastro"),
    path("login/", views.Login, name="Login"),
    path("home/", views.Home, name="Home"),
    path("perfil/", views.Perfil, name="Perfil"),
    path("agendamentos/", views.Agendamentos, name="Agendamentos"),
]