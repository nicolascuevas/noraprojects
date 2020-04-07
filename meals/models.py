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

from noraprojects.task import send_slack_notification
from meals import helpers


class Menu(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    #send = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(default=timezone.now, unique=True)
    #uuid = models.UUIDField(default=helpers.generate_uuid())

    class Meta:
        verbose_name = 'Menu'
        ordering = ['date']

    def __str__(self):
        return self.date

    def can_choose_menu(self):
        """
            Choose their preferred meal (until 11 AM CLT)
        """
        today_date = datetime.now()
        today_time = time(today_date.hour, today_date.minute, today_date.second)
        result = today_time.hour <= 10 and today_time.minute <= 60
        return result


class Option(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    description = models.CharField(max_length=370, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Option'

    def __str__(self):
        return self.description


class Order(models.Model):
    employee_identifier = models.CharField(max_length=10, null=True, blank=True)
    option = models.IntegerField(default=0, null=True, blank=True)
    menu = models.IntegerField(default=0, null=True, blank=True)
    customization = models.CharField(max_length=170, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Employee Order'

    def __str__(self):
        return self.employee_identifier


@receiver(post_save, sender=Menu)
def post_menu(instance, **kwargs):
    if False:
        options = Option.objects.filter(menu__id=instance.id)
        send_slack_notification(options, instance.uuid)
