# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.db.models import signals
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime, time
from meals import helpers

import uuid


class Menu(models.Model):
    user = models.ForeignKey(User, null=False, blank=False)
    enable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(default=timezone.now, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4)

    class Meta:
        verbose_name = 'Menu'
        ordering = ['date']


    def __str__(self):
        return str(self.date)


    def can_choose_menu(self):
        return helpers.before_lunch_time(self.date)


    def is_enable(self):
        return self.enable

    def get_order_count(self):
        return Order.objects.filter(menu=self).count()

    order_count = property(fget=get_order_count)


class Option(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    description = models.CharField(max_length=370, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Option'

    def __str__(self):
        return self.description

    def get_order_count(self):
        return Order.objects.filter(option=self).count()
    order_count = property(fget=get_order_count)



class Employee(models.Model):
    identifier = models.CharField(max_length=64, verbose_name="identifier", default=helpers.generate_uuid(), unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Employee'

    def __str__(self):
        return str(self.identifier)

    def __unicode__(self):
        return str(self.identifier)


class Order(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    option = models.ForeignKey(Option, on_delete=models.DO_NOTHING)
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)
    customization = models.CharField(max_length=170, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Employee Order'
        unique_together = ('menu', 'employee')

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if helpers.before_lunch_time(self.menu.date) == False:
            raise ValidationError("This Meal is closed")
        super(Order, self).save(*args, **kwargs)
