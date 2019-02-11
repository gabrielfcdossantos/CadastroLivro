from django import forms

class CadastroLivro(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    numpaginas = forms.IntegerField(label='Numero de Paginas')
