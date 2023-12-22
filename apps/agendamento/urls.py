from django.urls import path
from . import views

app_name = 'agendamento'

urlpatterns = [
    path('criar-agendamento/<int:horario_pk>/', views.CriarAgendamento.as_view(), name='criar-agendamento'), 
]
