from django.contrib import admin

# Register your models here.

from .models import Livro

class LivroAdmin(admin.ModelAdmin):

    list_display = ['name', 'num']




admin.site.register(Livro, LivroAdmin)
