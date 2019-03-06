# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-22 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventaregistrada',
            name='direccion',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ventaregistrada',
            name='nombre',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ventaregistrada',
            name='tarjeta',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]