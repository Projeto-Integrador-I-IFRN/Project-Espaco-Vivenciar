from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MaxLengthValidator, validate_integer
from django import forms
from django.contrib.auth.models import User, AbstractUser
from datetime import  datetime, time, timedelta
from django.core.exceptions import ValidationError

class Paciente(models.Model):

    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('Outro', 'Outro')
    ]

    nome_paciente = models.CharField('Nome', max_length = 200)
    data_nascimento = models.DateField('Data de Nascimento')
    genero = models.CharField('Sexo', max_length=24, choices = GENERO_CHOICES, null = True)
    email = models.EmailField(max_length= 200, unique = True, null = True)
    contato_paciente = models.CharField('Contato', max_length = 15, unique = True, null = True)

    cpf_paciente = models.CharField(
        max_length = 11,
        unique = True,
        null = True,
        validators=[
            validate_integer,
            MinLengthValidator(limit_value = 11, message ='O CPF deve ter exatamente 11 dígitos.'),
            MaxLengthValidator(limit_value = 11, message ='O CPF deve ter exatamente 11 dígitos.'),
        ]
    )

    def __str__(self):
        return f'Nome: {self.nome_paciente} CPF: {self.cpf_paciente}'
    
    def clean_cpf(self):
        cpf_paciente = self.cleaned_data['cpf_paciente']
        if len(cpf_paciente) != 11:
            raise forms.ValidationError('O CPF deve ter exatamente 11 caracteres.')
        return cpf_paciente
    
class Profissional(models.Model):
    imagem = models.ImageField(upload_to='media')
    numero_registro = models.CharField( verbose_name= 'Registro Profissional', max_length = 20)
    nome_medico = models.CharField('Nome', max_length = 200)
    especialidade = models.CharField('Especialidade', max_length = 200)
    contato_profissional = models.CharField('Contato', max_length = 15, unique = True, null = True )

    def __str__(self):
        return f'Nome: {self.nome_medico} - {self.especialidade}'
     
class Servico(models.Model):
    nome_servico = models.CharField('Nome', max_length= 200)
    duracao_horas = models.PositiveIntegerField()
    duracao_minutos = models.PositiveIntegerField()
    profissional = models.ForeignKey(Profissional, on_delete = models.CASCADE)

    def duracao_total_minutos(self):
        return self.duracao_horas * 60 + self.duracao_minutos

    def __str__(self):
        return f'Nome: {self.nome_servico}'
    
class AgendaMedica(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, null=True)
    data = models.DateField(null=True)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null=True)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    def get_duracao_servico(self):
        duracao_servico = timedelta(minutes=self.servico.duracao_total_minutos())
        return duracao_servico
    
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
                    fim = horario_fim_atendimento.time()
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
    agenda_medica = models.ForeignKey(AgendaMedica, on_delete= models.CASCADE, blank = True)
    inicio = models.TimeField()
    fim = models.TimeField()

    def __str__(self):
        return f'{self.inicio} - {self.fim}'

class Agendamento(models.Model):
    pass


class Atendente(models.Model):
    pass
