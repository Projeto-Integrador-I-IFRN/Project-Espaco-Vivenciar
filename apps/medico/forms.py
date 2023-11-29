from django import forms
from core.models import Profissional

class ProfissionalForm(forms.ModelForm):
    class Meta: 
        fields = '__all__'