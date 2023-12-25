from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, validate_integer
from django import forms
from django.conf import settings

class Paciente(models.Model):

    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('Outro', 'Outro')
    ]

    nome_paciente = models.CharField('Nome', max_length = 200)
    data_nascimento = models.DateField('Data de Nascimento')
    genero = models.CharField('Sexo', max_length=24, choices = GENERO_CHOICES, null = True)
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Nome: {self.nome_paciente} CPF: {self.cpf_paciente}'
    
    def clean_cpf(self):
        cpf_paciente = self.cleaned_data['cpf_paciente']
        if len(cpf_paciente) != 11:
            raise forms.ValidationError('O CPF deve ter exatamente 11 caracteres.')
        return cpf_paciente
    
