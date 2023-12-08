# Generated by Django 4.2.6 on 2023-12-06 20:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Atendente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_paciente', models.CharField(max_length=200, verbose_name='Nome')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('email', models.EmailField(max_length=200)),
                ('cpf_paciente', models.CharField(max_length=11, validators=[django.core.validators.validate_integer, django.core.validators.MinLengthValidator(limit_value=11, message='O CPF deve ter exatamente 11 dígitos.'), django.core.validators.MaxLengthValidator(limit_value=11, message='O CPF deve ter exatamente 11 dígitos.')])),
            ],
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='media')),
                ('nome_medico', models.CharField(max_length=200, verbose_name='Nome')),
                ('especialidade', models.CharField(max_length=200, verbose_name='Especialidade')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_servico', models.CharField(max_length=200, verbose_name='Nome')),
                ('duracao_servico', models.DurationField(verbose_name='Duração')),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profissional')),
            ],
        ),
    ]
