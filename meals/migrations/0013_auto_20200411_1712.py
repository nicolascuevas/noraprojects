# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-04-11 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0012_auto_20200411_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='identifier',
            field=models.CharField(default=b'a3770208043944c4a3ac2e6f155a3aad', max_length=64, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='option',
            name='description',
            field=models.CharField(default='dsa', max_length=370),
            preserve_default=False,
        ),
    ]
