from datetime import datetime

from django.db import models

class Produto(models.Model):
    data_de_publicacao = models.DateTimeField(default=datetime.now(), blank=True)
    informacoes = models.TextField(max_length=200)
    modelo = models.CharField(max_length=50)
    nome_do_produto = models.CharField(max_length=200)
    preco = models.CharField(max_length=20)
    tamanho = models.CharField(max_length=100)
