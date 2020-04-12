# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta
from random import randint

from django.contrib.auth.models import User
from django.test import TestCase

from meals import helpers
from meals.models import Menu, Option, Order, Employee
import uuid

from django.db import IntegrityError
import warnings
import exceptions



# Create your tests here.


class mealsTest(TestCase):


    def create_employee(self, identifier):
        return Employee.objects.create(identifier=identifier)

    def create_user(self, username="testuser", first_name="Test", last_name="User"):
        return User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_superuser=False,
            is_active=True,
            is_staff=False
        )

    def create_menu(self, user, title="Test Menu", date=datetime.now(), created_at=datetime.now(), updated_at=datetime.now()):

        return Menu.objects.create(
            user=user,
            date=date,
            title=title,
            created_at=created_at,
            updated_at=updated_at
        )

    def create_option(self, menu, description, created_at, updated_at):
        return Option.objects.create(
            menu=menu,
            description=description,
            created_at=created_at,
            updated_at=updated_at
        )

    def create_order(self, menu, option, employee, customization=""):
        return Order.objects.create(
                    employee=employee,
                    option=option,
                    menu=menu,
                    customization=customization
                )

##user Tests

    def test_user_creation(self):
        user = self.create_user("randomName", "firstName", "lastName")
        #get all users from db
        users = User.objects.all()
        #test quantity
        self.assertEquals(users.count(), 1)
        #test type
        self.assertTrue(isinstance(user, User))
        #test user info
        self.assertEquals(user.username, "randomName")
        self.assertEquals(user.first_name, "firstName")
        self.assertEquals(user.last_name, "lastName")

## Employee Test

    def test_employee_creation(self):
        employee = self.create_employee(helpers.generate_uuid())
        self.assertTrue(isinstance(employee, Employee))
        self.assertEqual(employee.__str__(), employee.identifier)

    def test_employee_uniqueness(self):
        generated_uuid = helpers.generate_uuid()
        employee_1 = self.create_employee(generated_uuid)
        with self.assertRaises(IntegrityError):
            self.create_employee(generated_uuid)



##Menu test

    def test_menu_creation(self):
        date = datetime( 2019, 10,10) ##arbitrary date
        user = self.create_user("randomName", "firstName", "lastName")
        menu = self.create_menu(user, "menuTitle", date, date, date)
        self.assertTrue(isinstance(menu, Menu))

    def test_menu_date_uniqueness(self):
        date = datetime( 2019, 10,10) ##arbitrary date
        user = self.create_user("randomName", "firstName", "lastName")
        menu_1 = self.create_menu(user, "menuTitle", date, date, date)
        with self.assertRaises(IntegrityError):
            self.create_menu(user, "menuTitle", date, date, date)



##Option Test

    def test_option_creation(self):
        date = datetime( 2019, 10,10) ##arbitrary date
        user = self.create_user("randomName", "firstName", "lastName")
        menu = self.create_menu(user, "menuTitle", date, date, date)
        option = self.create_option(menu ,"Arroz", datetime.now(), datetime.now())
        self.assertTrue(isinstance(option, Option))
        self.assertEqual(option.__str__(), option.description)
        self.assertTrue(option.description)

    def test_option_creation_with_null_description(self):
        date = datetime( 2019, 10,10) ##arbitrary date
        user = self.create_user("randomName", "firstName", "lastName")
        menu = self.create_menu(user, "menuTitle", date, date, date)
        with self.assertRaises(IntegrityError):
            self.create_option(menu , None, datetime.now(), datetime.now())


## Orders Test

    def test_order_creation_before_due_date(self):
        # edit and create is allowed to future dates
        date = datetime.now() + timedelta(1) 
        employee = self.create_employee(helpers.generate_uuid())
        user = self.create_user("randomName", "firstName", "lastName")
        menu = self.create_menu(user, "menuTitle", date, date, date)
        option = self.create_option(menu ,"Arroz", datetime.now(), datetime.now())
        customization = "customization example"
        order = self.create_order(menu, option, employee, customization)

        self.assertTrue(isinstance(order, Order))
        self.assertTrue(isinstance(order.menu, Menu))
        self.assertTrue(isinstance(order.employee, Employee))
        self.assertTrue(isinstance(order.option, Option))

    def test_order_edit_by_employee(self):
        # edit and create is allowed to future dates
        date = datetime.now() + timedelta(1) 
        employee = self.create_employee(helpers.generate_uuid())
        user = self.create_user("randomName", "firstName", "lastName")
        menu = self.create_menu(user, "menuTitle", date, date, date)
        option_1 = self.create_option(menu ,"Arroz", datetime.now(), datetime.now())
        option_2 = self.create_option(menu ,"Pure", datetime.now(), datetime.now())
        customization = "customization example"
        order = self.create_order(menu, option_1, employee, customization)
        #1 selection and count totals and count selection
        self.assertEqual(order.option.__str__(), "Arroz")
        self.assertEqual(option_1.order_count, 1)
        self.assertEqual(option_2.order_count, 0)
        self.assertEqual(order.menu.order_count, 1)
        ##change selection
        order.option = option_2
        order.save()
        self.assertTrue(isinstance(order, Order))
        ##counts validations
        self.assertEqual(order.option.__str__(), "Pure")
        self.assertEqual(option_1.order_count, 0)
        self.assertEqual(option_2.order_count, 1)
        self.assertEqual(order.menu.order_count, 1)

    ##test after due date 11pm Santiago



