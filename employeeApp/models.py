# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime, time

from myproj.task import send_slack_notification
from meals import helpers

# Create your models here.


class Employee(models.Model):
    identifier = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=70, null=True, blank=True)

    class Meta:
        verbose_name = 'Employee'

    def __str__(self):
        return self.email
