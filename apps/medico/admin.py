from django.contrib import admin
from .models import Profissional, Servico

# Register your models here.
@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome_medico', 'especialidade', 'contato_profissional', 'imagem')

@admin.register(Servico)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('nome_servico', 'duracao_servico', 'profissional')