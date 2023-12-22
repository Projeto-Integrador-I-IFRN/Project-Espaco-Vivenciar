from .models import Agendamento
from django import forms


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        exclude = ['horario_selecionado']
