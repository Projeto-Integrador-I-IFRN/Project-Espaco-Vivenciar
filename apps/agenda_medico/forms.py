from django import forms
from apps.medico.models import Profissional, Servico
from .models import AgendaMedica
import re
class SelecionarAgendaForm(forms.Form):
    servico = forms.ModelChoiceField(queryset=Servico.objects.none(), label='Selecione o serviço', widget=forms.Select(attrs={'class': 'edit-field'}))

    def __init__(self, *args, **kwargs):
        profissional = kwargs.pop('profissional', None)
        super(SelecionarAgendaForm, self).__init__(*args, **kwargs)
        if profissional:
            self.fields['servico'].queryset = profissional.servico_set.all()

class CustomDateInput(forms.DateInput):
    def format_value(self, value):
        if value:
            return value.strftime('%d/%m/%Y')
        return value

class AgendaMedicaForm(forms.ModelForm):
    data = forms.DateField(
        widget=CustomDateInput(attrs={'class': 'edit-field', 'placeholder': 'dd/mm/aaaa', 'type': 'date'}),
        input_formats=['%d/%m/%Y', '%Y/%m/%d', '%d-%m-%Y', '%Y-%m-%d'],
    )
    class Meta:
        model = AgendaMedica
        exclude = ['profissional', 'servico']
        widgets = {
        'horario_inicio': forms.TimeInput(attrs={'class': 'edit-field', 'placeholder': '00:00'}),
        'horario_fim': forms.TimeInput(attrs={'class': 'edit-field', 'placeholder': '00:00'}),
    }