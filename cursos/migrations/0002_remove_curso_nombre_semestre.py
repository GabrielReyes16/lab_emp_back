# Generated by Django 5.0 on 2023-12-15 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='nombre_semestre',
        ),
    ]
