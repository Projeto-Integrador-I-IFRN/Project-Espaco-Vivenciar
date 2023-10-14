from django.urls import path
from . import views

urlpatterns = [
    path("cadastro/", views.Cadastro, name="Cadastro"),
    path("perfil/", views.Perfil, name="Perfil"),
]