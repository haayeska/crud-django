# Portal de Alunos (CRUD com Django)

Sistema web para cadastrar, listar, buscar, editar e excluir alunos, feito com Django e Bootstrap.

## Funcionalidades

- Cadastro de alunos com nome, e-mail, matrícula, curso e data de nascimento
- Validação dos campos, com as mensagens de erro embaixo de cada um
- Matrícula única: não deixa cadastrar a mesma duas vezes
- Busca por nome, matrícula ou curso
- Edição em uma página própria
- Exclusão com confirmação, aceita só por `POST`
- Mensagens de sucesso depois de cada ação
- Painel administrativo do Django com busca e filtro por curso
- Testes automatizados das principais regras

## Tecnologias

- [Python 3.13](https://www.python.org/) e [Django 5.2](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/) para o visual
- SQLite como banco de dados

## Como rodar

Você precisa do [Python](https://www.python.org/downloads/) 3.10 ou mais novo.

```bash
git clone https://github.com/haayeska/crud-django.git
cd crud-django

# Crie e ative um ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux e macOS

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Depois abra http://localhost:8000.

Para usar o painel administrativo em http://localhost:8000/admin, crie um usuário com `python manage.py createsuperuser`.

## Testes

```bash
python manage.py test alunos
```

## Configuração

Sem nenhuma configuração, o projeto roda em modo de desenvolvimento. Para publicar, defina as variáveis de ambiente listadas em [`.env.example`](.env.example): `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0` e `DJANGO_ALLOWED_HOSTS`.

## Estrutura

```
alunos/
├── forms.py        # Formulário com as validações
├── models.py       # Modelo Aluno
├── views.py        # Listar, cadastrar, editar e excluir
├── urls.py
├── admin.py        # Configuração do painel administrativo
├── tests.py        # Testes automatizados
└── templates/alunos/
    ├── base.html   # Layout com menu e mensagens
    ├── lista.html  # Cadastro, busca e tabela
    ├── editar.html
    └── _campos.html  # Campos compartilhados entre cadastro e edição
portal/
└── settings.py     # Configurações do projeto
```
