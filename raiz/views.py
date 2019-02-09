# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Livro


# Create your views here.
def home(request):
    return render(request, 'home.html')

def lembrete(request):
    return render(request, 'lembrete.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')

def listagem(request):
    livros = Livro.objects.all()
    template_name = 'listagem.html'
    context = {
        'livros': livros
    }
    return render(request, template_name, context)
