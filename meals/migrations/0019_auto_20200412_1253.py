# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-04-12 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0018_auto_20200412_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='identifier',
            field=models.CharField(default=b'6b6bab75472c46c99fe76edc640fbde7', max_length=64, unique=True, verbose_name='identifier'),
        ),
    ]
