from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.paciente.forms import PacienteForm
from betterforms.multiform import MultiModelForm
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class SolicitarConsulta(forms.Form):
    campo1 = forms.CharField()
    campo2 = forms.IntegerField()
    
class PerfilUserForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form'}),
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form'}),
        help_text="Your password cannot be similar to the rest of your personal information.",
    )

    password2 = forms.CharField(
        label="Confirm your password",
        widget=forms.PasswordInput(attrs={'class': 'form'}),
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
