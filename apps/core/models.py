from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MaxLengthValidator, validate_integer
from django import forms

class Agendamento(models.Model):
    pass

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
    cpf_paciente = models.CharField(
        max_length=11,

        validators=[
            validate_integer,
            MinLengthValidator(limit_value=11, message='O CPF deve ter exatamente 11 dígitos.'),
            MaxLengthValidator(limit_value=11, message='O CPF deve ter exatamente 11 dígitos.'),
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
    nome_medico = models.CharField('Nome', max_length= 200)
    especialidade = models.CharField('Especialidade', max_length= 200)

    def __str__(self):
        return f'Nome: {self.nome_medico} - {self.especialidade}'
class Servico(models.Model):
    nome_servico = models.CharField('Nome', max_length= 200)
    duracao_servico = models.DurationField('Duração')
    profissional = models.ForeignKey(Profissional, on_delete= models.CASCADE)

    def __str__(self):
        return f'Nome: {self.nome_servico} '
    

