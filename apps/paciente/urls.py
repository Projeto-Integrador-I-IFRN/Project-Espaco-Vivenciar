from django.urls import path
from . import views

app_name = 'paciente'

urlpatterns = [

    path("atendente/pacientes/", views.ListarPacientes.as_view(), name="listar-pacientes"),
    path("atendente/pacientes/criar", views.CriarPaciente.as_view(), name="criar-paciente"),
    path("atendente/pacientes/excluir/<int:id>", views.ExcluirPaciente.as_view(), name="excluir-paciente"),
    path("atendente/pacientes/editar/<int:id>", views.EditarPaciente.as_view(), name="editar-paciente"),
]