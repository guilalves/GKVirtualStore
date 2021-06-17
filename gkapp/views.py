from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def produto(request):
    return render(request, 'produto.html')
