from django.contrib import admin
from .models import Paciente, Profissional, Servicos, Agendamento

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome_paciente', 'data_nascimento', 'genero', 'email', 'cpf_paciente')

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome_medico', 'especialidade', 'horario_inicial', 'horario_final')

@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('nome_servico', 'duracao_servico')

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_filter = ['profissional']