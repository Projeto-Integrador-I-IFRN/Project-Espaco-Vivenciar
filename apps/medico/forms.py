from django import forms
from apps.core.models import Profissional, Servico

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['imagem', 'nome_medico', 'especialidade']

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome_servico', 'duracao_servico']
