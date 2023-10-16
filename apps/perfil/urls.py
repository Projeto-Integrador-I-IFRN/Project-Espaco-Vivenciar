from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path("cadastro/", views.Cadastro, name="Cadastro"),
    path("login/", views.Login, name="Login"),
    path("perfil/", views.Perfil, name="Perfil"),
]