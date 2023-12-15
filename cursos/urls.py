from django.db import models
from django.urls import path
from .views import CursoView, CursoViewDetail, SemestreView, SemestreViewDetail, cursos_por_semestre

urlpatterns = [
    #Rutas con modelo Curso
    path('cursos/get', CursoView.as_view()),
    path('cursos/post', CursoView.as_view()),
    path('cursos/get/<int:pk>/', CursoViewDetail.as_view()),
    path('cursos/put/<int:pk>/', CursoViewDetail.as_view()),
    path('cursos/delete/<int:pk>/', CursoViewDetail.as_view()),
    path('cursos/por_semestre/<int:semestre_id>/', cursos_por_semestre, name='cursos_por_semestre'),
    #Rutas con modelo Semestre
    path('semestres/get', SemestreView.as_view()),
    path('semestres/post', SemestreView.as_view()),
    path('semestres/get/<int:pk>/', SemestreViewDetail.as_view()),
    path('semestres/put/<int:pk>/', SemestreViewDetail.as_view()),
    path('semestres/delete/<int:pk>/', SemestreViewDetail.as_view())
]