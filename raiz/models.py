from django.db import models
#from django.core.urlresolvers import reverse
# Create your models here.


class Livro(models.Model):
    name = models.CharField('Nome', max_length=100)
    num = models.IntegerField('Paginas')
    image = models.ImageField(upload_to='livros/image', verbose_name='Imagem',
     null=True, blank=True
     )
