# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-04-09 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApp', '0013_auto_20200409_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='identifier',
            field=models.CharField(default=uuid.UUID('1092fe63-7a98-11ea-bf78-b8e8563a0e58'), max_length=64, verbose_name='identifier'),
        ),
    ]
