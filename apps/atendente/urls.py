from django.urls import path
from . import views

app_name = 'atendente'

urlpatterns = [
    path("atendente/home/", views.Home, name="Home"),
    path("atendente/gerenciar-agenda/", views.GerenciarAgendas, name="Gerenciar-Agendas"),
    path("atendente/gerenciar-profissionais/", views.GerenciarProfissionais, name="Gerenciar-Profissionais"),
    path("atendente/gerenciar-pacientes/", views.GerenciarPacientes, name="Gerenciar-Pacientes"),
    path("atendente/cadastrar-profissionais/", views.CadastrarProfissionais, name="Cadastrar-Profissionais"),
    path("atendente/agendamentos-solicitacoes/", views.AgendamentosSolicitacoes, name="Agendamentos-Solicitacoes"),
    #path('atendente/modal2.html', views.mostrar_modal_atendente, name='ModalAtendente'),
]