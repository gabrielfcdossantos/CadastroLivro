from django.db import models
#from django.core.urlresolvers import reverse
# Create your models here.


class Livro(models.Model):
    name = models.CharField('Nome', max_length=100)
    num = models.IntegerField('Paginas')
    image = models.ImageField(upload_to='livros/image', verbose_name='Imagem',
     null=True, blank=True
     )


class Lembrete(models.Model):

    #name = models.CharField('Nome', max_length=100)
    data = models.DateTimeField()
    #data_criacao = models.DateTimeField('data_criacao', auto_now_add=True)
    livro = models.ForeignKey(Livro, on_delete = models.CASCADE)
