# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-04-12 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0013_auto_20200411_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='identifier',
            field=models.CharField(default=b'f0af54ea474342538342779cff317374', max_length=64, unique=True, verbose_name='identifier'),
        ),
    ]
