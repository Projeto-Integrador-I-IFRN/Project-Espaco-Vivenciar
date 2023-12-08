from django.db import models

# Create your models here.
class Profissional(models.Model):
    imagem = models.ImageField(upload_to='media')
    nome_medico = models.CharField('Nome', max_length = 200)
    especialidade = models.CharField('Especialidade', max_length = 200)
    contato_profissional = models.CharField('Contato', max_length = 15, unique = True, null = True )

    def __str__(self):
        return f'Nome: {self.nome_medico} - {self.especialidade}'
    
class Servico(models.Model):
    nome_servico = models.CharField('Nome', max_length= 200)
    duracao_servico = models.DurationField('Duração')
    profissional = models.ForeignKey(Profissional, on_delete = models.CASCADE)

    def __str__(self):
        return f'Nome: {self.nome_servico}'
    