from django.db import models
from datetime import  datetime, timedelta
from django.core.exceptions import ValidationError
from apps.medico.models import Profissional, Servico

class AgendaMedica(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete = models.PROTECT, null = True, blank = True)
    data = models.DateField()
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null = True, blank = True)
    horario_inicio = models.TimeField(verbose_name = 'Horário de início')
    horario_fim = models.TimeField(verbose_name = 'Horário de fim')

    def get_duracao_servico(self):
        if self.servico:
            duracao_servico = timedelta(minutes=self.servico.duracao_total_minutos())
            return duracao_servico
        return timedelta()
    
    def get_horario_inicio(self):
        horario_inicio = datetime.combine(self.data, self.horario_inicio)
        return horario_inicio
    
    def get_horario_fim(self):
        horario_fim = datetime.combine(self.data, self.horario_fim)
        return horario_fim
    
    def gerar_horarios_atendimento(self):
        duracao_servico = self.get_duracao_servico()
        horario_inicio = self.get_horario_inicio()
        horario_fim = self.get_horario_fim()

        while horario_inicio < horario_fim:
            horario_fim_atendimento = horario_inicio + duracao_servico

            if horario_fim_atendimento <= horario_fim:

                horario = Horario.objects.create(
                agenda_medica = self,
                inicio = horario_inicio.time(),
                fim = horario_fim_atendimento.time(),
                disponivel = True  # ou o valor apropriado para disponibilidade
                )

            horario_inicio += duracao_servico

    def clean(self):

        conflito = AgendaMedica.objects.filter(

            profissional = self.profissional,
            data = self.data,
            horario_inicio__lt = self.horario_fim,
            horario_fim__gt = self.horario_inicio

        ).exclude(pk = self.pk)  # Excluir a própria agenda ao editar
        horario_inicio = self.get_horario_inicio()
        horario_fim = self.get_horario_fim()
        duracao_servico = self.get_duracao_servico()
        intervalo_disponivel = horario_fim - horario_inicio

        if conflito.exists():
            raise ValidationError('Conflito de horários com outras agendas do mesmo profissional.')
        
        elif horario_inicio > horario_fim:
            raise ValidationError('O intervalo de horários é inválido!')
        
        elif intervalo_disponivel < duracao_servico:
            raise ValidationError('O tempo é insuficiente! se deseja continuar, aumente o horário da agenda.')


    def save(self, *args, **kwargs):
        self.full_clean()  # Chama a validação clean antes de salvar
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Agenda de {self.profissional.nome_medico} em {self.data}'
    
class Horario(models.Model):
    agenda_medica = models.ForeignKey(AgendaMedica, on_delete = models.CASCADE, blank = True, related_name = 'horario_selecionado')
    inicio = models.TimeField()
    fim = models.TimeField()
    disponivel = models.BooleanField( default = True)

    def __str__(self):
        return f'{self.inicio} - {self.fim} - {self.disponivel}'

