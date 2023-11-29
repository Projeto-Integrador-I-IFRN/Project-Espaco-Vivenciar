from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'medico'

urlpatterns = [
    path("atendente/profissionais/", views.GerenciarProfissionais, name="Gerenciar-Profissionais"),
    path("atendente/profissionais/cadastrar", views.CadastrarProfissionais, name="Cadastrar-Profissionais"),
    path("atendente/profissionais/criar", views.NovoProfissional, name='Novo-Profissional'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)