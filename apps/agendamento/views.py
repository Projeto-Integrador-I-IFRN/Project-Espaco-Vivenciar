from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import ListView, View, CreateView
from .models import Agendamento, Solicitacao
from .forms import AgendamentoForm, SolicitacaoForm
from apps.medico.models import Profissional, Servico
from apps.agenda_medico.models import AgendaMedica, Horario
from apps.paciente.models import Paciente
from django.contrib import messages
from django.contrib import messages
from django.urls import reverse

class CriarSolicitacao(View):
    
    def post(self, request, horario_pk, *args, **kwargs):
        horario = get_object_or_404(Horario, id=horario_pk)

        profissional_pk = horario.agenda_medica.profissional.pk
        servico_id = horario.agenda_medica.servico.id
        # Verifica se o horário está disponível
        if not horario.disponivel:
            messages.error(request, 'O horário selecionado não está disponível.')
            return redirect('paciente:listar-agendas', profissional_pk=profissional_pk, servico_id=servico_id)

        # Verifica se já existe uma solicitação para o mesmo horário
        if Solicitacao.objects.filter(horario_selecionado=horario).exists():
            messages.error(request, 'Já existe uma solicitação para este horário.')
            return redirect('paciente:listar-agendas', profissional_pk=profissional_pk, servico_id=servico_id)

        # Verifica se já existe um agendamento realizado para o mesmo horário
        if Agendamento.objects.filter(horario_selecionado=horario).exists():
            messages.error(request, 'Já existe um agendamento realizado para este horário.')
            return redirect('paciente:listar-agendas', profissional_pk=profissional_pk, servico_id=servico_id)

        paciente_id = self.request.user.id
        paciente = get_object_or_404(Paciente, user__id=paciente_id)

        # Cria a solicitação
        solicitacao = Solicitacao.objects.create(
            paciente=paciente,
            horario_selecionado=horario,
            agenda_medica=horario.agenda_medica
        )

        # Suponha que você precise extrair profissional_pk e servico_id da sua agenda_medica
        profissional_pk = solicitacao.agenda_medica.profissional.pk
        servico_id = solicitacao.agenda_medica.servico.pk

        messages.success(request, 'Solicitação realizada com sucesso!')

        # Adicione as mensagens à sessão antes de redirecionar
        for message in messages.get_messages(request):
            messages.add_message(request, message.level, message.message)

        # Use reverse para obter a URL reversa com argumentos
        url = reverse('paciente:listar-agendas', kwargs={'profissional_pk': profissional_pk, 'servico_id': servico_id})

        # Redirecione para a URL obtida
        return redirect(url)
    
class CriarAgendamento(CreateView):
    model = Agendamento
    template_name = 'agendamento/modal_selecionar_paciente.html'
    form_class = AgendamentoForm
    pk_url_kwarg = 'horario_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pacientes'] = Paciente.objects.all()
        context['horario_pk'] = self.kwargs.get('horario_pk')
        return context

    def form_valid(self, form):
        horario_pk = self.kwargs.get('horario_pk')
        horario = Horario.objects.get(id=horario_pk)
        paciente_id = self.request.POST.get('paciente_id')
        paciente = Paciente.objects.get(id=paciente_id)
        
        # Suponha que o Horario esteja associado a uma AgendaMedica
        agenda_medica = horario.agenda_medica
        
        horario.disponivel = False
        horario.save()

        form.instance.horario_selecionado = horario
        form.instance.paciente = paciente
        form.instance.agenda_medica = agenda_medica
        return super().form_valid(form)
        

    def get_success_url(self):
        horario_pk = self.kwargs.get('horario_pk')
        horario = Horario.objects.get(id=horario_pk)
        agenda_pk = horario.agenda_medica.pk
        print(agenda_pk)
        return reverse_lazy('agendamento:listar-agendamentos', kwargs={'agenda_pk': agenda_pk})


class AceitarRecusarSolicitacaoView(View):
    def post(self, request, solicitacao_id, action):
        solicitacao = get_object_or_404(Solicitacao, pk=solicitacao_id)

        if action == 'aceitar':
            # Verifica se há um horário selecionado e uma agenda médica associada
            if solicitacao.horario_selecionado and solicitacao.agenda_medica:
                Agendamento.objects.create(
                    paciente=solicitacao.paciente,
                    horario_selecionado=solicitacao.horario_selecionado,
                    agenda_medica=solicitacao.agenda_medica
                )
                solicitacao.aceitar_solicitacao()
                solicitacao.delete()
                return redirect(f'https://api.whatsapp.com/send?phone={solicitacao.paciente.contato_paciente}&text=Ol%C3%A1,%20seu%20agendamento%20no%20Espa%C3%A7o%20Vivenciar%20foi%20confirmado!', target='_blank')


        elif action == 'recusar':
            solicitacao.recusar_solicitacao()
            solicitacao.delete()

            return redirect(f'https://api.whatsapp.com/send?phone={solicitacao.paciente.contato_paciente}&text=Ol%C3%A1,%20infelizmente%20por%20motivos%20maiores%20venho%20informar%20n%C3%A3o%20ser%C3%A1%20poss%C3%ADvel%20realizar%20seu%20agendamento', target='_blank')
      


class ListarAgendamentosSolicitacoes(ListView):
    template_name = 'agendamento/agendamentos_solicitacoes.html'
    model = Agendamento

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipo_modelo = self.request.GET.get('tipo_modelo', 'agendamento')

        agenda_medica_id = self.kwargs.get('agenda_pk')
        agenda = AgendaMedica.objects.get(pk=agenda_medica_id)

        if tipo_modelo == 'agendamento':
            queryset = Agendamento.objects.filter(horario_selecionado__agenda_medica__id=agenda_medica_id)
        elif tipo_modelo == 'solicitacao':
            queryset = Solicitacao.objects.filter(horario_selecionado__agenda_medica__id=agenda_medica_id)
        else:
            queryset = Agendamento.objects.filter(horario_selecionado__agenda_medica__id=agenda_medica_id)

        context['itens'] = queryset.select_related('horario_selecionado__agenda_medica').all()
        context['tipo_modelo'] = tipo_modelo

        context['count_agendamentos'] = Agendamento.objects.filter(horario_selecionado__agenda_medica=agenda).count()

        context['count_solicitacoes'] = Solicitacao.objects.filter(horario_selecionado__agenda_medica=agenda).count()

        context['servico'] = agenda.servico.nome_servico
        context['dias_da_semana'] = self.listar_dias_semana(agenda)
        context['is_agendamento'] = isinstance(queryset.first(), Agendamento)
        context['agenda'] = agenda

        return context

    def listar_dias_semana(self, agenda):
        dias_da_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
        dia_semana_numero = agenda.data.weekday()
        return dias_da_semana[dia_semana_numero]

