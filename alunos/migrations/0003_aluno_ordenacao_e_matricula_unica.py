from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_remove_aluno_situacao_aluno_data_nascimento_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluno',
            options={'ordering': ['nome'], 'verbose_name': 'aluno', 'verbose_name_plural': 'alunos'},
        ),
        migrations.AlterField(
            model_name='aluno',
            name='curso',
            field=models.CharField(max_length=100, verbose_name='curso'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(verbose_name='data de nascimento'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(max_length=20, unique=True, verbose_name='matrícula'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='nome'),
        ),
    ]
