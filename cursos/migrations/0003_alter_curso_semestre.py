# Generated by Django 5.0 on 2023-12-15 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_remove_curso_nombre_semestre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='semestre',
            field=models.ForeignKey(blank=True, db_column='id_semestre', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cursos.semestre'),
        ),
    ]