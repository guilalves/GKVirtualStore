# Generated by Django 3.2.4 on 2021-06-22 22:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gkapp', '0009_alter_produto_data_de_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='data_de_publicacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 22, 19, 32, 29, 168992)),
        ),
    ]
