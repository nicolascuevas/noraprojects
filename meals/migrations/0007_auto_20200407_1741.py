# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-04-07 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0006_auto_20200407_1628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['date'], 'verbose_name': 'Menu'},
        ),
        migrations.AlterField(
            model_name='menu',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, unique=True),
        ),
    ]
