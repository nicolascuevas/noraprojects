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

import uuid

# Create your models here.


class Employee(models.Model):
    identifier = models.UUIDField(primary_key=True, null= False, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=70, null=False, blank=True)
    name = models.CharField(max_length=10, null=False, blank=True)
    slack_id = models.CharField(max_length=20, null=False, blank=True, unique=True)

    class Meta:
        verbose_name = 'Employee'

    def __str__(self):
        return str(self.identifier)

    def __unicode__(self):
        return str(self.identifier)

