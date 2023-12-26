from django.db import models
from apps.paciente.models import Paciente
from apps.medico.models import Profissional
from apps.agenda_medico.models import Horario, AgendaMedica
from django.core.exceptions import ValidationError

class Solicitacao(models.Model):
    CHOICES = [
        ('P', 'Pendente'),
        ('A', 'Aceito'),
        ('R', 'Recusado')
    ]

    paciente = models.ForeignKey( to = Paciente, on_delete = models.PROTECT, blank=True)
    horario_selecionado = models.ForeignKey(to = Horario, on_delete = models.PROTECT, blank = True)
    status = models.CharField(max_length = 20, choices = CHOICES, default = 'P', blank = True)
    agenda_medica = models.ForeignKey(AgendaMedica, on_delete=models.CASCADE, related_name='solicitacoes', blank = True) 

    def alterar_disponibilidade_horario(self, disponibilidade):
        self.horario_selecionado.disponivel = disponibilidade
        self.horario_selecionado.save()

    def aceitar_solicitacao(self):
        if self.status == 'P':
            self.status = 'A'
            self.save()
            self.alterar_disponibilidade_horario(False)
        
    def recusar_solicitacao(self):
        if self.status == 'P':
            self.status = 'R'
            self.save()
            self.alterar_disponibilidade_horario(True)

    def __str__(self):
        return f'Solicitação de {self.paciente.nome_paciente} em {self.horario_selecionado} para o procedimento: {self.horario_selecionado.agenda_medica.servico.nome_servico}'
    
    def clean(self):
        if not self.horario_selecionado.disponivel:
            raise ValidationError('O horário selecionado não está disponível.')

    def save(self, *args, **kwargs):
    
        if not self.pk:  # Verifica se é uma nova solicitação
            # Marca o horário como indisponível ao criar uma nova solicitação
            self.alterar_disponibilidade_horario(False)

        super().save(*args, **kwargs)
        print("Solicitação salva com sucesso!")

    class Meta:
        verbose_name_plural = 'Solicitações'

class Agendamento(models.Model):
    paciente = models.ForeignKey( to = Paciente, on_delete = models.PROTECT, blank=True)
    horario_selecionado = models.OneToOneField(to = Horario, on_delete = models.PROTECT, null = True,blank=True)
    agenda_medica = models.ForeignKey(AgendaMedica, on_delete=models.CASCADE, related_name='agendamentos', blank = True)  # Add related_name