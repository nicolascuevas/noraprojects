# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-04-09 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0011_auto_20200409_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='employee_identifier',
        ),
        migrations.AlterField(
            model_name='menu',
            name='uuid',
            field=models.UUIDField(default=b'b6a564d19f3044d8b5b31c449565afa9'),
        ),
    ]
