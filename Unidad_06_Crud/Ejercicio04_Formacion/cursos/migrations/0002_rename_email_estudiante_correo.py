# Generated by Django 4.2.17 on 2025-02-10 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='email',
            new_name='correo',
        ),
    ]
