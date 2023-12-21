import random
import locale
from faker import Faker
from django.core.files import File
from django.core.management.base import BaseCommand
from apps.medico.models import Profissional, Servico
import urllib.request
from io import BytesIO

fake = Faker('pt_BR')  # Configuração para usar dados em português
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Configuração para formatar números em português

class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        # Criar profissionais fictícios
        for _ in range(5):
            imagem_url = fake.image_url()
            imagem_temp = BytesIO(urllib.request.urlopen(imagem_url).read())
            imagem = File(imagem_temp)

            print(f'Imagem criada: {imagem}')  # Mensagem de depuração

            registro = fake.unique.random_number(digits=10)
            nome = fake.name()
            especialidade = fake.job()
            contato = fake.random_int(min=100000000000000, max=999999999999999)  # Números de contato com até 15 dígitos

            profissional = Profissional.objects.create(
                imagem=imagem,
                numero_registro=registro,
                nome_medico=nome,
                especialidade=especialidade,
                contato_profissional=str(contato)  # Garantir que o número de contato seja uma string
            )
            self.stdout.write(self.style.SUCCESS(f'Profissional criado: {profissional}'))

            # Criar serviços fictícios para cada profissional
            for _ in range(5):
                nome_servico = fake.bs()
                duracao_horas = random.randint(0, 2)
                duracao_minutos = random.randint(0, 59)

                Servico.objects.create(
                    nome_servico=nome_servico,
                    duracao_horas=duracao_horas,
                    duracao_minutos=duracao_minutos,
                    profissional=profissional
                )
                self.stdout.write(self.style.SUCCESS(f'Serviço criado para {profissional}: {nome_servico}'))

        self.stdout.write(self.style.SUCCESS('Dados fictícios foram adicionados com sucesso!'))
