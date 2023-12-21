
from django.urls import path
from . import views

app_name = 'agenda_medico'

urlpatterns = [
    path("atendente/home/", views.Home.as_view(), name="Home"),
    path('selecionar-agenda/<int:profissional_pk>/', views.SelecionarAgendaView.as_view(), name='selecionar_agenda'),
    path('agenda/<int:profissional_pk>/<int:servico_id>/', views.ListarAgenda.as_view(), name='listar-agenda'),
    path('agenda/horarios-de-atendimento<int:agenda_id>', views.ListarHorarios.as_view(), name='listar-horarios'),   
]
