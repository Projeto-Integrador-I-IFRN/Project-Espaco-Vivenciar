# utils.py
from apps.agenda_medico.models import AgendaMedica

def obter_dia_semana_por_agenda_id(agenda_id):
    try:
        agenda = AgendaMedica.objects.get(id=agenda_id)
        dia_semana_numero = agenda.data.weekday()
        dias_da_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
        return dias_da_semana[dia_semana_numero]
    except AgendaMedica.DoesNotExist:
        return None
