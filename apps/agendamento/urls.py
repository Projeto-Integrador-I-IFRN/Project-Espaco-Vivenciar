from django.urls import path
from . import views

app_name = 'agendamento'

urlpatterns = [
    path('criar-agendamento/<int:horario_pk>/', views.CriarAgendamento.as_view(), name='criar-agendamento'), 
    path('agenda/agendamentos/<int:agenda_pk>/', views.ListarAgendamentos.as_view(), name='listar-agendamentos'), 
]
