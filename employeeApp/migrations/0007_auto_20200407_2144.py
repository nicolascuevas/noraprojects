# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-04-08 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApp', '0006_auto_20200407_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='identifier',
            field=models.UUIDField(),
        ),
    ]
