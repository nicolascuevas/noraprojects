# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from datetime import datetime

from django.contrib.auth.decorators import login_required
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




def today_menu(request, uuid):
    
    template = "meals/menu_show_today.html"
    #find session emplooye token or create and asign one for identification
    employee = get_object_or_404(Employee ,identifier=request.session['employee_token'] ) if 'employee_token' in request.session else Employee.objects.create(identifier=generate_uuid())
    request.session['employee_token'] = str(employee.identifier)
    #show the menu based on uuid
    menu = get_object_or_404(Menu, uuid=uuid)
    #get option for the current menu
    options = Option.objects.filter(menu=menu)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.employee = employee
            instance = form.save(commit=False)
            instance.save
            #order_instance = map_form_to_order(form, menu, employee)
            #order_instance.save()
            messages.success(
                request, "Choice added successfully", extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('meals:selected_menu')
        else:
            print "error"
    
    form = OrderForm(instance=Order.objects.all()[0])
    context = {'options': options, 'form': form, 'menu': menu}

    if Order.objects.filter(menu=menu, employee=employee).exists():
        order = Order.objects.get(menu=menu, employee=employee)
        print "camino"
        context = {'options': options, 'form': form, 'menu': menu, 'order': order}
        return render(request, template, context)
    return render(request, template, context)



def map_form_to_order(form, menu, employee):
    option = Option.objects.get(pk=int(form.cleaned_data['option']))
    customization = form.cleaned_data['customization']

    if Order.objects.filter(menu=menu, employee=employee).exists():
        order = Order.objects.get(menu=menu, employee=employee)
        order.customization = customization
        order.option = option
        return order
    else:
        return Order(menu=menu, employee=employee, option=option, customization=customization)

    return False


def today_menu_show(request, uuid):
    template = "meals/menu_show_selection.html"
    menu = get_object_or_404(Menu, uuid=uuid)

    context = {}

    return render(request, template, context)



