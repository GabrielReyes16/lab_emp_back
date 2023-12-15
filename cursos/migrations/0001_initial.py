# Generated by Django 5.0 on 2023-12-15 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id_semestre', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'db_table': 'semestre',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=200)),
                ('nombre_semestre', models.CharField(blank=True, max_length=50)),
                ('semestre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cursos.semestre')),
            ],
            options={
                'db_table': 'curso',
                'managed': True,
            },
        ),
    ]