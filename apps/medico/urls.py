# apps/medico/urls.py

from django.urls import path
from . import views

app_name = 'medico'

urlpatterns = [
    path("atendente/profissionais/", views.ListarProfissionais.as_view(), name="listar-profissionais"),
    path("atendente/profissionais/cadastrar", views.CriarProfissional.as_view(), name="Cadastrar-Profissionais"),
    path('criar/servico/<int:profissional_pk>/', views.CriarServico.as_view(), name='criar-servico'),
    path('servico/', views.ListarServico.as_view(), name='listar-servico'),
    path('excluir-servico/<int:servico_pk>/<int:profissional_pk>/', views.ExcluirServico.as_view(), name='excluir-servico'),
    path('editar-servico/<int:servico_pk>/<int:profissional_pk>/', views.EditarServico.as_view(), name='editar-servico'),
    path("atendente/profissional/excluir/<int:id>", views.ExcluirProfissional.as_view(), name="excluir-profissional"),
    path('detalhe-profissional/<int:profissional_pk>/', views.DetalharProfissional.as_view(), name='detalhe-profissional'),
    path('editar-profissional/<int:profissional_pk>/', views.EditarProfissional.as_view(), name='editar-profissional'),

    
]
