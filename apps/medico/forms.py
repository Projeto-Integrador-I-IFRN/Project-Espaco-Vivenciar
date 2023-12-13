from django import forms
from apps.medico.models import Profissional, Servico
from django.forms import inlineformset_factory

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = '__all__'
        widgets = {
        'nome_medico' : forms.TextInput(attrs={'class': 'edit-field' }),
        'especialidade' : forms.TextInput(attrs={'class': 'edit-field' }),
        'numero_registro' : forms.TextInput(attrs={'class': 'edit-field' }),
        'contato_profissional' : forms.TextInput(attrs={'class': 'edit-field' }),
        'imagem' : forms.FileInput(attrs={'class': 'edit-field' }),

        
    }

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        exclude = ['profissional']
        widgets = {
        'nome_servico' : forms.TextInput(attrs={'class': 'edit-field' }),
        'duracao_horas': forms.NumberInput(attrs={'class': 'edit-field'}),
        'duracao_minutos': forms.NumberInput(attrs={'class': 'edit-field'}),
    }
