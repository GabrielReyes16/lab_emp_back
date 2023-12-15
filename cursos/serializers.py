from rest_framework import serializers
from .models import Curso, Semestre


class SemestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semestre
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    semestre = SemestreSerializer(read_only=True)

    class Meta:
        model = Curso
        fields = '__all__'
