from django import forms
from apps.medico.models import Profissional, Servico
from django.forms import inlineformset_factory

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = '__all__'

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'

# ProfissionalServicoFormSet = inlineformset_factory(Profissional, Servico, form=ServicoForm, extra=1, can_delete=True)
