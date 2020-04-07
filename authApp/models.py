# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from .signals import assign_admin_role


models.signals.post_save.connect(assign_admin_role, sender=User)


