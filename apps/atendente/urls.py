from django.urls import path
from . import views

app_name = 'atendente'

urlpatterns = [
    path("atendente/agendamentos/", views.AgendamentosSolicitacoes, name="Agendamentos-Solicitacoes"),
    #path('atendente/modal2.html', views.mostrar_modal_atendente, name='ModalAtendente'),
]