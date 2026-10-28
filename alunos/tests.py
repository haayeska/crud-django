from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse

from .models import Aluno


def dados_aluno(**extras):
    dados = {
        'nome': 'Maria Souza',
        'email': 'maria@exemplo.com',
        'matricula': '2025001',
        'curso': 'Sistemas de Informação',
        'data_nascimento': '2000-05-10',
    }
    dados.update(extras)
    return dados


class CadastroTests(TestCase):
    def test_cadastra_aluno_valido(self):
        resposta = self.client.post(reverse('lista_alunos'), dados_aluno())
        self.assertRedirects(resposta, reverse('lista_alunos'))
        self.assertEqual(Aluno.objects.count(), 1)

    def test_campo_vazio_mostra_erro_sem_salvar(self):
        resposta = self.client.post(reverse('lista_alunos'), dados_aluno(nome=''))
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(Aluno.objects.count(), 0)

    def test_matricula_repetida_nao_e_aceita(self):
        Aluno.objects.create(**dados_aluno(data_nascimento=date(2000, 5, 10)))
        self.client.post(reverse('lista_alunos'), dados_aluno(nome='Outra Pessoa'))
        self.assertEqual(Aluno.objects.count(), 1)

    def test_nascimento_no_futuro_nao_e_aceito(self):
        amanha = (date.today() + timedelta(days=1)).isoformat()
        self.client.post(reverse('lista_alunos'), dados_aluno(data_nascimento=amanha))
        self.assertEqual(Aluno.objects.count(), 0)


class EdicaoEExclusaoTests(TestCase):
    def setUp(self):
        self.aluno = Aluno.objects.create(**dados_aluno(data_nascimento=date(2000, 5, 10)))

    def test_edita_aluno(self):
        url = reverse('editar_aluno', args=[self.aluno.id])
        self.client.post(url, dados_aluno(curso='Engenharia de Software'))
        self.aluno.refresh_from_db()
        self.assertEqual(self.aluno.curso, 'Engenharia de Software')

    def test_exclusao_por_get_e_recusada(self):
        resposta = self.client.get(reverse('excluir_aluno', args=[self.aluno.id]))
        self.assertEqual(resposta.status_code, 405)
        self.assertTrue(Aluno.objects.exists())

    def test_exclusao_por_post(self):
        self.client.post(reverse('excluir_aluno', args=[self.aluno.id]))
        self.assertFalse(Aluno.objects.exists())

    def test_busca_filtra_pela_matricula(self):
        Aluno.objects.create(**dados_aluno(nome='João', matricula='999', data_nascimento=date(2001, 1, 1)))
        resposta = self.client.get(reverse('lista_alunos'), {'q': '999'})
        self.assertContains(resposta, 'João')
        self.assertNotContains(resposta, 'Maria Souza')
