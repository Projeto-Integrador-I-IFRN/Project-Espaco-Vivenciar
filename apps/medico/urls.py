# apps/medico/urls.py

from django.urls import path
from . import views

app_name = 'medico'

urlpatterns = [
    path("atendente/profissionais/", views.ListarProfissionais.as_view(), name="listar-profissionais"),
    path("atendente/profissionais/cadastrar", views.CriarProfissional.as_view(), name="Cadastrar-Profissionais"),
    path('criar/servico/<int:profissional_pk>/', views.CriarServico.as_view(), name='criar-servico'),
    path('servico/', views.ListarServico.as_view(), name='listar-servico'),
    path("atendente/profissional/excluir/<int:id>", views.ExcluirProfissional.as_view(), name="excluir-profissional"),
]
