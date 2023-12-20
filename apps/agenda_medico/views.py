from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, View
from apps.medico.models import Profissional
from .models import AgendaMedica
from .forms import SelecionarAgendaForm
from django.views.generic.edit import FormView

class Home(ListView):
    model = Profissional
    template_name = 'agenda_medico/home.html'
    context_object_name = 'profissionais'

class SelecionarAgendaView(FormView):
    template_name = 'agenda_medico/modal_escolher_agenda.html'
    form_class = SelecionarAgendaForm
    pk_url_kwarg = 'profissional_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profissional_pk = self.kwargs.get('profissional_pk')
        profissional = Profissional.objects.get(pk=profissional_pk)
        context['profissional'] = profissional
        context['servicos'] = profissional.servico_set.all()
        return context

    def form_valid(self, form):
        profissional_pk = self.kwargs.get('profissional_pk')
        profissional = Profissional.objects.get(pk=profissional_pk)
        servico = form.cleaned_data['servico']
        agendas = AgendaMedica.objects.filter(servico=servico)

        return render(
            self.request,
            'atendente/gerenciar_agenda.html',
            {'profissional': profissional, 'servico': servico, 'agendas': agendas}
        )
    
    def get_form_kwargs(self):
        kwarg = super().get_form_kwargs()
        profissional_pk = self.kwargs.get('profissional_pk')
        profissional = Profissional.objects.get(pk=profissional_pk)
        kwarg['profissional'] = profissional

        return kwarg
