import random
from faker import Faker
from django.core.management.base import BaseCommand
from apps.paciente.models import Paciente
from cpf_generator import CPF

fake = Faker('pt_BR')

class Command(BaseCommand):
    help = 'Populate the database with fake patient data'

    def handle(self, *args, **kwargs):
        for _ in range(50):
            nome_paciente = fake.name()
            data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=80)
            genero = random.choice(['M', 'F', 'Outro'])
            email = fake.email()
            contato_paciente = fake.phone_number()

            # Gerar CPF válido
            cpf_paciente = CPF.generate()

            Paciente.objects.create(
                nome_paciente=nome_paciente,
                data_nascimento=data_nascimento,
                genero=genero,
                email=email,
                contato_paciente=contato_paciente,
                cpf_paciente=cpf_paciente
            )
            self.stdout.write(self.style.SUCCESS(f'Paciente criado: {nome_paciente}'))

        self.stdout.write(self.style.SUCCESS('Dados fictícios de pacientes foram adicionados com sucesso!'))
