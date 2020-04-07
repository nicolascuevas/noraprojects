# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls.base import reverse_lazy
from django.views import generic

from . import forms


class LoginTemplateView(auth_views.LoginView):
    template_name = 'authApp/login.html'
    redirect_field_name = 'next'

    def get_success_url(self):
        if self.request.user.groups.filter(name__iexact='admin').exists() \
                or self.request.user.is_superuser:
            return reverse_lazy('list_menu')
        elif self.request.user.groups.filter(name__iexact='employees').exists():
            return reverse_lazy('authApp:home')


class RegisterView(generic.CreateView):
    form_class = forms.RegisterForm
    template_name = 'authApp/signup.html'
    success_url = reverse_lazy('authApp:login')
