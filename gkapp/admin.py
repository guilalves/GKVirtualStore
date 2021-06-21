from django.contrib import admin

from .models import Produto


class ListaProdutos(admin.ModelAdmin):
    list_display = (
        'id', 'nome_do_produto', 'modelo', 'tamanho', 'data_de_publicacao', 'preco', 'publicado'
        )
    list_display_links = ('id', 'nome_do_produto')
    list_filter = ('modelo', )
    list_per_page = 10
    list_editable = ('publicado', )
    search_fields = ('nome_do_produto', )


admin.site.register(Produto, ListaProdutos)
