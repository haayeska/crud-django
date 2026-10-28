from datetime import date

from django import forms

from .models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'matricula', 'curso', 'data_nascimento']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome completo'}),
            'email': forms.EmailInput(attrs={'placeholder': 'nome@exemplo.com'}),
            'matricula': forms.TextInput(attrs={'placeholder': 'Ex.: 2025001'}),
            'curso': forms.TextInput(attrs={'placeholder': 'Ex.: Análise e Desenvolvimento de Sistemas'}),
            # format garante que o valor salvo apareça no campo ao editar
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica as classes do Bootstrap em todos os campos de uma vez
        for campo in self.fields.values():
            campo.widget.attrs['class'] = 'form-control'

    def full_clean(self):
        super().full_clean()
        # Deixa a borda vermelha do Bootstrap nos campos com erro
        for nome in self.errors:
            if nome in self.fields:
                self.fields[nome].widget.attrs['class'] += ' is-invalid'

    def clean_nome(self):
        return ' '.join(self.cleaned_data['nome'].split())

    def clean_matricula(self):
        return self.cleaned_data['matricula'].strip()

    def clean_data_nascimento(self):
        nascimento = self.cleaned_data['data_nascimento']
        if nascimento > date.today():
            raise forms.ValidationError('A data de nascimento não pode estar no futuro.')
        return nascimento
