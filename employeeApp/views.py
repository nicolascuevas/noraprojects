# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, redirect
from meals.models import Menu, Option, Order
from employeeApp.models import Employee
from django.template import Context, Template
from django.http import HttpResponse
import datetime
import uuid

# Create your views here.


def employee_meal_choose(request, user_uuid):
    method = "GET"
    message = "Selecciona La Opción que más te guste."
    template = 'employeeApp/employee_meal_choose.html'
    user_uuid = uuid.UUID(user_uuid).hex
    employee = Employee.objects.get(identifier=user_uuid)

    current_date = datetime.datetime.now()
    year = current_date.strftime("%Y")
    month = current_date.strftime("%m")
    day = current_date.strftime("%d")
    current_menu = Menu.objects.filter(date__year=year, date__month=month, date__day=day)
    if len(current_menu) > 0:
        current_menu = current_menu[0]
    else:
        current_menu = Menu.objects.all()[0]

    options = Option.objects.filter(menu__id=current_menu.id)

    if request.method == "POST":
        if not request.POST.get("option_id") or  not request.POST.get("employee_id") or  not request.POST.get("menu_id") or current_menu.can_choose_menu == False:
            return HttpResponse('Missing Information', status=403)
        choosen_option = options[0]
        if request.POST.get("option_id"):
            choosen_option = Option.objects.filter(id=request.POST.get("option_id"))[0]
        choosen_menu = Menu.objects.filter(id=request.POST.get("menu_id"))[0]
        customization = request.POST.get("customization")
        

        if len( Order.objects.filter(employee_identifier=user_uuid, menu__id=choosen_menu.id) ) == 0:
            order = Order(
                menu=choosen_menu,
                option=choosen_option,
                employee_identifier=employee,
                customization=customization
            )
            order.save()
        else:
            order = Order.objects.filter(employee_identifier=user_uuid, menu=choosen_menu)[0]
            order.customization = customization
            order.option = choosen_option
            order.save()

        method = "POST"
        message = "Seleccionaste Exitosamente: " + choosen_option.description + "\n \n"
        message += "\n, especificacion:"
        message += "\n" + customization

    context = {
        'menu': current_menu,
        'options': options,
        'employee': employee,
        'method': method,
        'message': message
    }

    return render(request, template, context)
