# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-30 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_producttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]
