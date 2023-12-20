from django import forms
from apps.medico.models import Profissional, Servico

class SelecionarAgendaForm(forms.Form):
    servico = forms.ModelChoiceField(queryset=Servico.objects.none(), label='Selecione o serviço', widget=forms.Select(attrs={'class': 'edit-field'}))

    def __init__(self, *args, **kwargs):
        profissional = kwargs.pop('profissional', None)
        super(SelecionarAgendaForm, self).__init__(*args, **kwargs)
        if profissional:
            self.fields['servico'].queryset = profissional.servico_set.all()
