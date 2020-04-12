# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import *
from rest_framework.views import APIView
from rest_framework.response import Response
from helpers import generate_uuid
from meals.models import Menu, Option, Order, Employee
from forms import OrderForm
from django.contrib.auth.mixins import PermissionRequiredMixin
import datetime
import uuid

from noraprojects.task import send_slack_notification


class BuildTrigger(APIView):
  def post(self, request):
    build_something() # This would take 1 minute to finish
    return Response(None, status=201)

@method_decorator(login_required, name='dispatch')
class ListOrder(ListView):
    template_name = "orders_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        menu_orders = Order.objects.filter(menu=self.kwargs['pk'])
        orders = []
        for order in menu_orders:
            option = Option.objects.filter(id=order.option.id).first()
            employee = Employee.objects.filter(identifier=order.employee).first()
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



class CreateOrder(CreateView):
    model = Order
    template_name = 'meals/employee_meal_choose.html'
    form_class = OrderForm


    def get_initial(self, **kwargs):
        initials = super(CreateOrder, self).get_initial()
        menu = Menu.objects.get(uuid=self.kwargs.get("uuid"))
        initials['menu'] = menu
        initials['options'] = Option.objects.filter(menu=menu)
        return initials

    def get(self, request, uuid, *args, **kwargs):
        form = self.form_class(initial=self.get_initial())
        employee = get_object_or_404(Employee ,identifier=self.request.session['employee_token'] ) if 'employee_token' in self.request.session else Employee.objects.create(identifier=generate_uuid())
        menu = Menu.objects.get(uuid=self.kwargs.get("uuid"))
        if Order.objects.filter(menu=menu, employee=employee).exists():
            return redirect(reverse_lazy('meals:selected_menu', kwargs={'uuid': uuid})) 
        ##set session identifier
        request.session['employee_token'] = str(employee.identifier)
        #redirect to edit if iser alreadt orders
        return render(request, self.template_name, {'form': form, 'menu': menu})

    def form_valid(self, form):
        employee = get_object_or_404(Employee ,identifier=self.request.session['employee_token'] ) if 'employee_token' in self.request.session else Employee.objects.create(identifier=generate_uuid())
        menu = Menu.objects.get(uuid=self.kwargs.get("uuid"))
        form.instance.employee = employee
        form.instance.menu = menu
        return super(CreateOrder, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('meals:selected_menu', kwargs={'uuid': self.object.menu.uuid})



class UpdateOrder(UpdateView):
    model = Order
    template_name = 'meals/employee_meal_choose.html'
    form_class = OrderForm

    def get_initial(self):
        initial = super(UpdateOrder, self).get_initial()
        order = Order.objects.get(pk=self.kwargs.get("pk"))
        initial['menu'] = Menu.objects.get(pk=order.menu.id)
        initial['option'] = order.option
        initial['customization'] = order.customization
        return initial

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.get_initial())
        employee = get_object_or_404(Employee ,identifier=self.request.session['employee_token'] ) if 'employee_token' in self.request.session else Employee.objects.create(identifier=generate_uuid())
        request.session['employee_token'] = str(employee.identifier)
        order = Order.objects.get(pk=self.kwargs.get("pk"))
        menu = order.menu
        if employee != order.employee:
            return redirect(reverse_lazy('meals:selected_menu', kwargs={'uuid': uuid}))
        print self.kwargs.get("pk")
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        return super(UpdateOrder, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('meals:selected_menu', kwargs={'uuid': self.object.menu.uuid})



def today_menu_show(request, uuid):
    template = "meals/menu_show_selection.html"
    employee = get_object_or_404(Employee ,identifier=request.session.get('employee_token', None) )
    menu = Menu.objects.get(uuid=uuid)
    order = Order.objects.filter(employee=employee, menu=menu)
    options = Option.objects.filter(menu=menu)
    if order.exists():
        order = order[0]
        option = order.option
        context = {'order': order, 'options': options, 'option': option, 'menu': menu}
        return render(request, template, context)

    else:
        return redirect(reverse_lazy('meals:today_menu_show', kwargs={'uuid': uuid}))





