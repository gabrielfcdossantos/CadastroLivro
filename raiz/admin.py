from django.contrib import admin

# Register your models here.

from .models import Livro
from .models import Lembrete

class LivroAdmin(admin.ModelAdmin):

    list_display = ['name', 'num']


class LembreteAdmin(admin.ModelAdmin):

    list_display = ['data', 'livro']




admin.site.register(Livro, LivroAdmin)
admin.site.register(Lembrete, LembreteAdmin)
