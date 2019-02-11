from django import forms
from .models import Livro

class CadastroLivro(forms.ModelForm):

    class Meta:
        model = Livro
        fields = ( 'name', 'num')
