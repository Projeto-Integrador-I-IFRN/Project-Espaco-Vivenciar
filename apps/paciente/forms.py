from django import forms
from apps.paciente.models import Paciente

class PacienteForm(forms.ModelForm):
    nome_paciente = forms.CharField(
        label="Nome do Paciente",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    data_nascimento = forms.DateField(
        label="Data de Nascimento",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )

    cpf_paciente = forms.CharField(
        label="CPF do Paciente",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXX.XXX.XXX-XX'}),
    )

    genero = forms.ChoiceField(
        label="Gênero",
        choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')],
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    contato_paciente = forms.CharField(
        label="Contato",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    class Meta:
        model = Paciente
        fields = ['nome_paciente', 'data_nascimento', 'cpf_paciente', 'genero', 'contato_paciente']
