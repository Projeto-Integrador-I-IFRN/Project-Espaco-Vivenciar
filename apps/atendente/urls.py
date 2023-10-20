from django.urls import path
from . import views

app_name = 'atendente'

urlpatterns = [
    path("atendente/home/", views.Home, name="Home"),
    path("atendente/gerenciar/", views.Gerenciar, name="Gerenciar"),
]