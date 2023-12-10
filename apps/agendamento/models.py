from django.db import models
from apps.paciente.models import Paciente
from apps.medico.models import Profissional
from apps.agenda_medico.models import Horario, AgendaMedica

class Agendamento(models.Model):
    paciente = models.ForeignKey( to = Paciente, on_delete = models.DO_NOTHING )

