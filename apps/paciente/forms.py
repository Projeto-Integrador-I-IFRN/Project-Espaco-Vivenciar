from django import forms
from apps.paciente.models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
        'nome_paciente' : forms.TextInput(attrs={'class': 'edit-field' }),
        'data_nascimento' : forms.DateInput(attrs={'class': 'edit-field' }),
        'genero' : forms.Select(attrs={'class': 'edit-field' }),
        'cpf_paciente' : forms.TextInput(attrs={'class': 'edit-field' }),
        'email' : forms.TextInput(attrs={'class': 'edit-field' }),
        'contato_paciente' : forms.TextInput(attrs={'class': 'edit-field' }),
    }