from django.urls import path
from . import views

app_name = 'atendente'

urlpatterns = [
    path("atendente/home/", views.Home, name="Home"),
    path("atendente/gerenciar/", views.Gerenciar, name="Gerenciar"),
    path("atendente/gerenciar-profissionais/", views.GerenciarProfissionais, name="Gerenciar-Profissionais"),
    path("atendente/cadastrar-profissionais/", views.CadastrarProfissionais, name="Cadastrar-Profissionais"),
    path('atendente/modal2.html', views.mostrar_modal_atendente, name='ModalAtendente'),
]