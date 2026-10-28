from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import AlunoForm
from .models import Aluno


def lista_alunos(request):
    """Mostra a lista de alunos e cadastra um novo pelo formulário da mesma página."""
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save()
            messages.success(request, f'{aluno.nome} foi cadastrado.')
            return redirect('lista_alunos')
    else:
        form = AlunoForm()

    busca = request.GET.get('q', '').strip()
    alunos = Aluno.objects.all()
    if busca:
        alunos = alunos.filter(
            Q(nome__icontains=busca) | Q(matricula__icontains=busca) | Q(curso__icontains=busca)
        )

    return render(request, 'alunos/lista.html', {'form': form, 'alunos': alunos, 'busca': busca})


def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, f'Os dados de {aluno.nome} foram atualizados.')
            return redirect('lista_alunos')
    else:
        form = AlunoForm(instance=aluno)

    return render(request, 'alunos/editar.html', {'form': form, 'aluno': aluno})


# Só aceita POST: um link (GET) não pode apagar dados
@require_POST
def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    messages.success(request, f'{aluno.nome} foi excluído.')
    return redirect('lista_alunos')
