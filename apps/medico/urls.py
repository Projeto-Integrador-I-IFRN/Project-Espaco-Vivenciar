from django.urls import path
from . import views

app_name = 'medico'

urlpatterns = [
    path("atendente/profissionais/", views.GerenciarProfissionais, name="Gerenciar-Profissionais"),
    path("atendente/profissionais/cadastrar", views.CadastrarProfissionais, name="Cadastrar-Profissionais"),
    path("atendente/profissionais/criar", views.NovoProfissional, name='Novo-Profissional'),

]

