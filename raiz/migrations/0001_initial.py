# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-02-09 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('num', models.IntegerField(verbose_name='Paginas')),
                ('image', models.ImageField(blank=True, null=True, upload_to='livros/image', verbose_name='Imagem')),
            ],
        ),
    ]
