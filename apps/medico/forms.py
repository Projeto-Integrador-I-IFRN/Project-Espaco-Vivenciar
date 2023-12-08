from django import forms
from apps.core.models import Profissional, Servico
from django.forms import inlineformset_factory

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['imagem', 'nome_medico', 'especialidade']

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'

# ProfissionalServicoFormSet = inlineformset_factory(Profissional, Servico, form=ServicoForm, extra=1, can_delete=True)
