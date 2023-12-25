from django.urls import path
from . import views

app_name = 'paciente'

urlpatterns = [

    path("atendente/pacientes/", views.ListarPacientes.as_view(), name="listar-pacientes"),
    path("atendente/pacientes/criar", views.CriarPaciente.as_view(), name="criar-paciente"),
    path("atendente/pacientes/excluir/<int:id>", views.ExcluirPaciente.as_view(), name="excluir-paciente"),
    path("atendente/pacientes/editar/<int:id>", views.EditarPaciente.as_view(), name="editar-paciente"),
    path("paciente/home/", views.Home.as_view(), name="Home"),
    
    path('paciente/selecionar-agenda/<int:profissional_pk>/', views.SelecionarAgendaView.as_view(), name='selecionar_agenda'),
    path('paciente/agenda/<int:profissional_pk>/<int:servico_id>/', views.ListarAgenda.as_view(), name='listar-agendas'),
    path('agenda/solicitar/<int:agenda_id>', views.ListarHorarios.as_view(), name='listar-horarios-atendimento'),   
]