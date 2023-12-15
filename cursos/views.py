from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import CursoSerializer, SemestreSerializer
from rest_framework.views import APIView
from .models import Curso, Semestre
from rest_framework.decorators import api_view

# Create your views here.

class CursoView(APIView):
    def get(self, request, format=None):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CursoViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Curso.objects.get(pk=pk)
        except Curso.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        curso = self.get_object(pk)
        serializer = CursoSerializer(curso)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        curso = self.get_object(pk)
        serializer = CursoSerializer(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        curso = self.get_object(pk)
        curso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SemestreView(APIView):
    def get(self, request, format=None):
        semestres = Semestre.objects.all()
        serializer = SemestreSerializer(semestres, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SemestreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SemestreViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Semestre.objects.get(pk=pk)
        except Semestre.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        semestre = self.get_object(pk)
        serializer = SemestreSerializer(semestre)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        semestre = self.get_object(pk)
        serializer = SemestreSerializer(semestre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        semestre = self.get_object(pk)
        semestre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def cursos_por_semestre(request, semestre_id):
    cursos = Curso.objects.filter(id_semestre=semestre_id)
    serializer = CursoSerializer(cursos, many=True)
    return Response(serializer.data)