from django.db import models


class Aluno(models.Model):
    nome = models.CharField('nome', max_length=100)
    email = models.EmailField('e-mail')
    curso = models.CharField('curso', max_length=100)
    matricula = models.CharField('matrícula', max_length=20, unique=True)
    data_nascimento = models.DateField('data de nascimento')

    class Meta:
        ordering = ['nome']
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'

    def __str__(self):
        return self.nome
