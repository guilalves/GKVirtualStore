from django.contrib import admin

from .models import Produto

class ListaProdutos(admin.ModelAdmin):
    list_display = ('id',
                    'nome_do_produto',
                    'modelo',
                    'tamanho',
                    'data_de_publicacao',
                    'preco')

    list_display_links = ('id', 'nome_do_produto')

admin.site.register(Produto, ListaProdutos)
