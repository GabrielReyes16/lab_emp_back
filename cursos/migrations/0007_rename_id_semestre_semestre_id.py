# Generated by Django 5.0 on 2023-12-15 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_alter_curso_options_alter_semestre_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semestre',
            old_name='id_semestre',
            new_name='id',
        ),
    ]
