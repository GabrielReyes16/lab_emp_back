# Generated by Django 5.0 on 2023-12-15 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0008_rename_id_semestre_id_semestre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='semestre',
            new_name='id_semestre',
        ),
    ]
