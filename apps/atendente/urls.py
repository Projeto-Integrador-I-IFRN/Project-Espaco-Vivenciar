from django.urls import path
from . import views

app_name = 'atendente'

urlpatterns = [
    path("atendente/home/", views.Home.as_view(), name="Home"),
    path("atendente/agenda/", views.GerenciarAgendas, name="Gerenciar-Agendas"),
    path("atendente/agendamentos/", views.AgendamentosSolicitacoes, name="Agendamentos-Solicitacoes"),
    #path('atendente/modal2.html', views.mostrar_modal_atendente, name='ModalAtendente'),
]