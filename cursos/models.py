from django.db import models

# Modelo Semestre


class Semestre(models.Model):
    id_semestre = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = 'semestre'


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=200, blank=True)
    id_semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'curso'
