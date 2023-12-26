from django import forms
from apps.paciente.models import Paciente

class PacienteForm(forms.ModelForm):
    nome_paciente = forms.CharField(
        label="Nome do Paciente",
        widget=forms.TextInput(attrs={'class': 'edit-field'}),
    )

    data_nascimento = forms.DateField(
        label="Data de Nascimento",
        widget=forms.DateInput(attrs={'class': 'edit-field', 'type': 'date'}),
    )

    cpf_paciente = forms.CharField(
        label="CPF do Paciente",
        widget=forms.TextInput(attrs={'class': 'edit-field', 'maxlength': '11'}),
    )

    genero = forms.ChoiceField(
        label="Gênero",
        choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')],
        widget=forms.Select(attrs={'class': 'edit-field'}),
    )

    contato_paciente = forms.CharField(
        label="Contato",
        widget=forms.TextInput(attrs={'class': 'edit-field'}),
    )
    class Meta:
        model = Paciente
        fields = ['nome_paciente', 'data_nascimento', 'cpf_paciente', 'genero', 'contato_paciente',]
