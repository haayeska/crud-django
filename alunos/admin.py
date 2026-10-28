from django.contrib import admin

from .models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'curso', 'email', 'data_nascimento']
    search_fields = ['nome', 'matricula', 'email']
    list_filter = ['curso']
