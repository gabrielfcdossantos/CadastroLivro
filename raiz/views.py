# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Livro
from .models import Lembrete
from .forms import CadastroLivro
from .forms import CadastroLembrete


# Create your views here.
def home(request):
    return render(request, 'home.html')





def lembrete(request):
    template_name = 'lembrete.html'
    form = CadastroLembrete(request.POST or None)
    context = {
        'form': form
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return render(request, template_name, context)






def cadastrar(request):

    template_name = 'cadastrar.html'

    form = CadastroLivro(request.POST or None)
    context = {
        'form': form
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        #    l = Livro()
        #    l = request.POST

            #import pdb; pdb.set_trace()

    return render(request, template_name, context)







def listagem(request):
    livros = Livro.objects.all()
    template_name = 'listagem.html'
    context = {
        'livros': livros
    }
    return render(request, template_name, context)
