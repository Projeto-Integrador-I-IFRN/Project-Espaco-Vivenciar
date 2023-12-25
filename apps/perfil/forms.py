from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PerfilUser
from apps.paciente.models import Paciente

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
        model = PerfilUser
        fields = ['email', 'password1', 'password2']
