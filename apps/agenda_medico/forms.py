from django import forms
from apps.medico.models import Profissional, Servico
from .models import AgendaMedica
class SelecionarAgendaForm(forms.Form):
    servico = forms.ModelChoiceField(queryset=Servico.objects.none(), label='Selecione o serviço', widget=forms.Select(attrs={'class': 'edit-field'}))

    def __init__(self, *args, **kwargs):
        profissional = kwargs.pop('profissional', None)
        super(SelecionarAgendaForm, self).__init__(*args, **kwargs)
        if profissional:
            self.fields['servico'].queryset = profissional.servico_set.all()

class AgendaMedicaForm(forms.ModelForm):
        class Meta:
            model = AgendaMedica
            exclude = ['profissional', 'servico']
            widgets = {
            'data' : forms.DateInput(attrs={'class': 'edit-field' }),
            'horario_inicio': forms.TimeInput(attrs={'class': 'edit-field'}),
            'horario_fim': forms.TimeInput(attrs={'class': 'edit-field'}),
        }