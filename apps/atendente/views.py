from django.shortcuts import render
from apps.medico.models import Profissional
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
# from .forms import NovaAgenda
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy

# Create your views here.

# def mostrar_modal_atendente(request):
#     form = NovaAgenda()
#     return render(request, 'atendente/modal2.html', {'form': form})
