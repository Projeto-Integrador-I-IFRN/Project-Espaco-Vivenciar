
from django.urls import path
from . import views

app_name = 'agenda_medico'

urlpatterns = [
    path("atendente/home/", views.Home.as_view(), name="Home"),
    path('selecionar-agenda/<int:profissional_pk>/', views.SelecionarAgendaView.as_view(), name='selecionar_agenda'),
    path('listar-agenda/<int:profissional_pk>/<int:servico_id>/', views.ListarAgenda.as_view(), name='listar-agenda')
,
    # path('listar-agendas/<int:profissional_pk>/<int:servico_pk>/', views.ListarAgendasView.as_view(), name='listar-agendas'),
]
