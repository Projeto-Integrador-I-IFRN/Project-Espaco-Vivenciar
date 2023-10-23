# nome_do_seu_app/forms.py
from django import forms

class NovaAgenda(forms.Form):
    campo1 = forms.CharField()
    campo2 = forms.IntegerField()
