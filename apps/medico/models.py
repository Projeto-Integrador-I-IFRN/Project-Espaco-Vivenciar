from django.db import models
from django.db.models import ProtectedError

class Profissional(models.Model):
    imagem = models.ImageField(upload_to =' media')
    numero_registro = models.CharField( verbose_name= 'Registro Profissional', max_length = 20)
    nome_medico = models.CharField('Nome', max_length = 200)
    especialidade = models.CharField('Especialidade', max_length = 200)
    contato_profissional = models.CharField('Contato', max_length = 15, unique = True, null = True )

    def __str__(self):
        return f'Nome: {self.nome_medico} - {self.especialidade}'
    
    class Meta:
        verbose_name_plural = 'Profissionais'
     
class Servico(models.Model):
    nome_servico = models.CharField('Nome', max_length= 200)
    duracao_horas = models.PositiveIntegerField( default= 0)
    duracao_minutos = models.PositiveIntegerField( default= 0)
    profissional = models.ForeignKey(Profissional, on_delete = models.CASCADE)

    def duracao_total_minutos(self):
        return self.duracao_horas * 60 + self.duracao_minutos

    def __str__(self):
        return f'Nome: {self.nome_servico}'
    