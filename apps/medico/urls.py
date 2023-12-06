from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'medico'

urlpatterns = [
    path("atendente/profissionais/", views.ListarProfissionais.as_view(), name="listar-profissionais"),
    path("atendente/profissionais/cadastrar", views.CriarProfissional.as_view(), name="Cadastrar-Profissionais"),
    path('adicionar-servico/', views.CriarServico.as_view(), name='criar-servico'),
    path('servico/', views.ListarServico.as_view(), name='listar-servico'),

]
