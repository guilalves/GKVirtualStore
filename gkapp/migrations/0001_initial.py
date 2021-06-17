# Generated by Django 3.2.4 on 2021-06-17 03:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_de_publicacao', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('nome_do_produto', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=50)),
                ('preco', models.CharField(max_length=20)),
                ('tamanho', models.CharField(max_length=50)),
            ],
        ),
    ]