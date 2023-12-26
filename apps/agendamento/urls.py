from django.urls import path
from . import views

app_name = 'agendamento'

urlpatterns = [
    path('criar-agendamento/<int:horario_pk>/', views.CriarAgendamento.as_view(), name='criar-agendamento'), 
    path('agenda/agendamentos/<int:agenda_pk>/', views.ListarAgendamentosSolicitacoes.as_view(), name='listar-agendamentos'),
    path('aceitar_recusar_solicitacao/<int:solicitacao_id>/<str:action>/', views.AceitarRecusarSolicitacaoView.as_view(), name='aceitar_recusar_solicitacao'),
    path('solicitar-agendamento/<int:horario_pk>/', views.CriarSolicitacao.as_view(), name='solicitar-agendamento'),

]
