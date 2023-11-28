from django.urls import path
from . import views

app_name = 'atendente'

urlpatterns = [
    path("atendente/home/", views.Home, name="Home"),
    path("atendente/agenda/", views.GerenciarAgendas, name="Gerenciar-Agendas"),
    path("atendente/profissionais/", views.GerenciarProfissionais, name="Gerenciar-Profissionais"),
    path("atendente/profissionais/cadastrar", views.CadastrarProfissionais, name="Cadastrar-Profissionais"),
    path("atendente/agendamentos/", views.AgendamentosSolicitacoes, name="Agendamentos-Solicitacoes"),
    path("atendente/profissionais/criar", views.NovoProfissional, name='Novo-Profissional'),
    #path('atendente/modal2.html', views.mostrar_modal_atendente, name='ModalAtendente'),

    path("atendente/pacientes/", views.ListarPacientes.as_view(), name="listar-pacientes"),
    path("atendente/pacientes/criar", views.CriarPaciente.as_view(), name="criar-paciente"),
    path("atendente/pacientes/excluir/<int:id>", views.ExcluirPaciente.as_view(), name="excluir-paciente"),
    path("atendente/pacientes/editar/<int:id>", views.EditarPaciente.as_view(), name="editar-paciente"),
]