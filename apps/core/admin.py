from django.contrib import admin
from apps.paciente.models import Paciente 
from apps.medico.models import Profissional, Servico
from apps.agenda_medico.models import AgendaMedica, Horario
from apps.agendamento.models import Agendamento

from django import forms

class HorarioInline(admin.TabularInline):  # ou StackedInline, dependendo da sua preferência visual
    model = Horario
    extra = 0  # Isso define o número inicial de formulários vazios para exibir no inline

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome_paciente', 'data_nascimento', 'genero', 'email', 'cpf_paciente')

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome_medico', 'especialidade', 'contato_profissional', 'imagem')

@admin.register(Servico)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('nome_servico', 'duracao_horas', 'duracao_minutos', 'profissional')

class HorarioAdmin(admin.ModelAdmin):
    list_display = ['inicio', 'fim']

class AgendaMedicaAdminForm(forms.ModelForm):
    class Meta:
        model = AgendaMedica
        exclude = []

    def clean(self):
        cleaned_data = super().clean()
        # Adicione qualquer lógica de validação adicional necessária aqui

@admin.register(AgendaMedica)
class AgendaMedicaAdmin(admin.ModelAdmin):
    form = AgendaMedicaAdminForm
    list_display = ['profissional', 'data', 'servico', 'horario_inicio', 'horario_fim']
    inlines = [HorarioInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.gerar_horarios_atendimento()

admin.site.register(Horario, HorarioAdmin)
