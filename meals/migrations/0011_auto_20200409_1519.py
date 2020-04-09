# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-04-09 19:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employeeApp', '0013_auto_20200409_1519'),
        ('meals', '0010_auto_20200408_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='enable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menu',
            name='uuid',
            field=models.UUIDField(default=b'b583c9dbd9ec4218a02669df75e8ec05'),
        ),
        migrations.AddField(
            model_name='order',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='employeeApp.Employee'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='order',
            unique_together=set([('menu', 'employee')]),
        ),
    ]