from django.db import models
from django.utils import timezone

class Atendente(models.Model):
    pass

class Paciente(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino')    
    ]

    nome_paciente = models.CharField('Nome', max_length= 200)
    data_nascimento = models.DateField('Data de Nascimento')
    genero = models.CharField('Sexo', max_length=24, choices=GENERO_CHOICES, null=True)
    email = models.EmailField(max_length= 200)
    cpf_paciente = models.CharField('cpf', max_length= 11, unique=True)

    def __str__(self):
        return f'Nome: {self.nome_paciente}'

class Servicos(models.Model):
    nome_servico = models.CharField('Nome', max_length= 200)
    duracao_servico = models.DurationField('Duração')

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return f'Nome: {self.nome_servico} '
    
class Profissional(models.Model):
    imagem = models.ImageField(upload_to='media')
    nome_medico = models.CharField('Nome', max_length= 200)
    especialidade = models.CharField('Especialidade', max_length= 200)
    horario_inicial = models.TimeField('Horário de Início', null=True)
    horario_final = models.TimeField('Horário de Término', null=True)
    servicos = models.ManyToManyField(Servicos, verbose_name='Serviços')

    def __str__(self):
        return f'Nome: {self.nome_medico}'

class Agendamento(models.Model):
    data_agendamento = models.DateTimeField(default=timezone.now)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, null=True)
    motivo_consulta = models.ForeignKey(Servicos, on_delete=models.CASCADE, default=1 ,limit_choices_to={'profissional__id': models.OuterRef('profissional')})

