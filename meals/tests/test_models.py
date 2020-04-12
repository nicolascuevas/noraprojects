# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
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

    def create_order(self, menu, option, user_uuid, customization):
        return Order.objects.create(
                    employee_identifier=user_uuid,
                    option=option,
                    menu=menu,
                    customization="any customization"
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

    # def test_order_creation(self):
    #     menu = self.create_menu("testuser", "Test", "User", "Test Menu", datetime.now(), datetime.now())
    #     option = self.create_option(menu ,"Arroz", datetime.now(), datetime.now())
    #     employee = self.create_employee(helpers.generate_uuid(), "applicant26dsa6", "slackuser")
    #     user_uuid = uuid.UUID(employee.identifier).hex

    #     order = self.create_order(menu, option, user_uuid, "any customization")

    #     self.assertTrue(isinstance(order, Order))
