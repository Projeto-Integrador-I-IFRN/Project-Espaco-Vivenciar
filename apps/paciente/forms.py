from django import forms
from apps.paciente.models import Paciente
from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

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
        label="Cpf",
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
        fields = ['nome_paciente', 'data_nascimento', 'cpf_paciente', 'genero', 'contato_paciente']

    def save(self, commit=True):
        # Garante que a instância do paciente esteja associada ao formulário antes de salvar
        paciente = super().save(commit=False)
        paciente.nome_paciente = self.cleaned_data['nome_paciente']
        paciente.data_nascimento = self.cleaned_data['data_nascimento']
        paciente.cpf_paciente = self.cleaned_data['cpf_paciente']
        paciente.genero = self.cleaned_data['genero']
        paciente.contato_paciente = self.cleaned_data['contato_paciente']

        if commit:
            paciente.save()

        return paciente

class PerfilUserForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'edit-field'}),
    )

    password1 = forms.CharField(
        label=("Senha"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'edit-field'}),
        help_text="Your password cannot be similar to the rest of your personal information.",
    )

    password2 = forms.CharField(
        label="Confirmar senha",
        widget=forms.PasswordInput(attrs={'class': 'edit-field'}),
        strip=False,
        help_text="Enter the same password entered previously for verification.",
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class UserProfileMultiForm(MultiModelForm):
    form_classes = {
        'perfiluser': PerfilUserForm,
        'pacienteuser': PacienteForm,
    }
