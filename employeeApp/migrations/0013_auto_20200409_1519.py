# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-04-09 19:19
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApp', '0012_auto_20200408_0320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='slack_id',
        ),
        migrations.AddField(
            model_name='employee',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='identifier',
            field=models.CharField(default=uuid.UUID('f7d40b80-7a96-11ea-b9bc-b8e8563a0e58'), max_length=64, verbose_name='Activation key'),
        ),
    ]