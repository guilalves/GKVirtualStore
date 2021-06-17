from django.shortcuts import render


def index(request):
    produtos = {
        1: 'Chaleira esmaltada Cupcake',
        2: 'Biscuit',
        3: 'Chaleira esmaltada Porquinho',
    }
    dados = {
        'nome_dos_produtos': produtos
    }
    return render(request, 'index.html', dados)


def produto(request):
    return render(request, 'produto.html')
