from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('alunos/<int:id>/editar/', views.editar_aluno, name='editar_aluno'),
    path('alunos/<int:id>/excluir/', views.excluir_aluno, name='excluir_aluno'),
]
