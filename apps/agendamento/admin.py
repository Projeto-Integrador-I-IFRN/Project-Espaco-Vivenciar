from django.contrib import admin
from .models import Agendamento

# Register your models here.
@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_filter = ('profissional')