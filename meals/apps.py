# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class MealsConfig(AppConfig):
    name = 'meals'

    def ready(self):
        import meals.signals
