# Generated by Django 4.2.6 on 2023-11-29 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_servico_duracao_servico_servico_nome_servico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='duracao_servico',
        ),
    ]