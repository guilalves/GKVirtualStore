from django.shortcuts import  get_list_or_404, get_object_or_404, render

from .models import Produto


def index(request):
    produtos = Produto.objects.all()

    dados = {
        'produtos': produtos
    }
    return render(request, 'index.html', dados)


def produto(request, produto_id):
    try:
        produto = get_object_or_404(Produto, pk=produto_id)
        produto_a_exibir = {
                'produto': produto
        }
    except Exception:
        print('ERROR! Nao foi possivel obter as informacoes dos produtos.')

    return render(request, 'produto.html', produto_a_exibir)
