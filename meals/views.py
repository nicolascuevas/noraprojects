# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import *

from forms import OrderForm
from meals.models import Menu, Option, Order
from employeeApp.models import Employee


@method_decorator(login_required, name='dispatch')
class ListOrder(ListView):
    template_name = "orders_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        menu_orders = Order.objects.filter(menu=self.kwargs['pk'])
        orders = []
        for order in menu_orders:
            option = Option.objects.filter(pk=order.option).first()
            employee = Employee.objects.filter(identifier=order.employee_identifier).first()
            orders.append(
                {
                    'order': order,
                    'option': option,
                    'employee': employee
                }
            )
        return orders


@method_decorator(login_required, name='dispatch')
class ListMenu(ListView):
    template_name = "menu_list.html"
    model = Menu
    context_object_name = 'menu'

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Menu.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class CreateMenu(CreateView):
    template_name = 'menu_add.html'
    model = Menu
    fields = ('title', 'date',)
    success_url = reverse_lazy('meals:list_menu')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateMenu, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class UpdateMenu(UpdateView):
    model = Menu
    fields = ('title', 'date',)
    template_name = 'menu_add.html'
    success_url = reverse_lazy('meals:list_menu')


@method_decorator(login_required, name='dispatch')
class ListOption(ListView):
    template_name = "menu_option.html"
    model = Option
    context_object_name = 'option'

    def get_queryset(self):
        return Option.objects.filter(menu__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        ctx = super(ListOption, self).get_context_data(**kwargs)
        ctx['menu'] = Menu.objects.get(pk=self.kwargs['pk'])
        return ctx


@method_decorator(login_required, name='dispatch')
class CreateOption(CreateView):
    template_name = 'menu_option_add.html'
    model = Option
    fields = ('description',)

    def form_valid(self, form):
        menu = Menu.objects.get(pk=self.kwargs['pk'])
        form.instance.menu = menu
        return super(CreateOption, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('meals:list_option', kwargs={'pk': self.object.menu.pk})


@method_decorator(login_required, name='dispatch')
class UpdateOption(UpdateView):
    model = Option
    fields = ('description',)
    template_name = 'menu_option_add.html'

    def get_success_url(self):
        return reverse_lazy('meals:list_option', kwargs={'pk': self.object.menu.pk})


def today_menu(request, uuid):
    date = datetime.today()
    menu = Menu.objects.get(created_at__year=date.year,
                            created_at__month=date.month,
                            created_at__day=date.day,
                            uuid=uuid)

    options = Option.objects.filter(menu=menu)

    if request.method == 'POST':
        form = OrderForm(request.POST, options=options)
        if form.is_valid():
            order_instance = map_form_to_order(form, menu)
            order_instance.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = OrderForm(options=options)

    context = {'options': options, 'form': form, 'menu': menu}
    template = "menu_show_today.html"
    return render(request, template, context)


def map_form_to_order(form, menu):
    order_instance = Order()
    order_instance.created_at = datetime.now()
    order_instance.employee_identifier = form.cleaned_data['employee_identifier']
    order_instance.option = int(form.cleaned_data['option'])
    order_instance.customization = form.cleaned_data['customization']
    order_instance.menu = menu.id
    return order_instance

