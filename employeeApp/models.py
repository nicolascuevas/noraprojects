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


# class Employee(models.Model):
#     identifier = models.CharField(max_length=64, verbose_name="identifier", default=uuid.uuid1())

#     class Meta:
#         verbose_name = 'Employee'

#     def __str__(self):
#         return str(self.identifier)

#     def __unicode__(self):
#         return str(self.identifier)


