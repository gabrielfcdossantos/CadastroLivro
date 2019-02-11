from django import forms
from .models import Livro
from .models import Lembrete

class CadastroLivro(forms.ModelForm):

    class Meta:
        model = Livro
        fields = ( 'name', 'num')

class CadastroLembrete(forms.ModelForm):

    class Meta:
        model = Lembrete
        fields = ('data','livro')
