from django import forms
from core.models import Profissional, Servico

class ProfissionalForm(forms.ModelForm):
    class Meta: 
        fields = '__all__'

class ServicoForm(forms.ModelForm):
    class Meta: 
        fields = '__all__'