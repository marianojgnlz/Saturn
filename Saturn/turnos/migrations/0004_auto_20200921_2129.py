# Generated by Django 3.1 on 2020-09-22 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0003_turno_idusuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turno',
            old_name='idusuario',
            new_name='usuario',
        ),
    ]
