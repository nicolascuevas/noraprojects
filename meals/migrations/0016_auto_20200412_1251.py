# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-04-12 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0015_auto_20200412_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='identifier',
            field=models.CharField(default=b'caecaa6b11264463be5a2d7e07e39495', max_length=64, unique=True, verbose_name='identifier'),
        ),
    ]
