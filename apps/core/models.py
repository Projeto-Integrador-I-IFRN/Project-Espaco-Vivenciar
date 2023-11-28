from django.db import models

class Agendamento(models.Model):
    pass

class Atendente(models.Model):
    pass

class Paciente(models.Model):
    nome_paciente = models.CharField('Nome', max_length= 200)
    data_nascimento = models.DateField('Data de Nascimento')
    email = models.EmailField(max_length= 200)
    cpf_paciente = models.CharField('cpf', max_length= 11)

    def __str__(self):
        return f'Nome: {self.nome_paciente} CPF: {self.cpf_paciente}'

class Profissional(models.Model):
    pass

class Servico(models.Model):
    pass
