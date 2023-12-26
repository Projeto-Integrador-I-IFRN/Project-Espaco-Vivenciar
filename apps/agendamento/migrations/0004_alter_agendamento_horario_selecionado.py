# Generated by Django 4.2.6 on 2023-12-25 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda_medico', '0001_initial'),
        ('agendamento', '0003_alter_agendamento_horario_selecionado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='horario_selecionado',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='agenda_medico.horario'),
        ),
    ]
