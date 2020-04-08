# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from random import randint

from django.contrib.auth.models import User
from django.test import TestCase

from meals import helpers
from meals.models import Menu, Option, Order
from employeeApp.models import Employee
import uuid


# Create your tests here.


class ModelsTest(TestCase):
    def create_employee(self, identifier, name, slack_id):
        employee = Employee(identifier=identifier, name=name, slack_id=slack_id)
        employee.save()
        return employee

    def create_user(self, username="testuser", first_name="Test", last_name="User"):
        return User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_superuser=False,
            is_active=True,
            is_staff=False
        )

    def create_menu(self, username, first_name, last_name, title="Test Menu",
                    created_at=datetime.now(), updated_at=datetime.now()):

        return Menu.objects.create(
            user=self.create_user(username, first_name, last_name),
            created_at=created_at,
            updated_at=updated_at,
            title=title,
            date= created_at
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

    def test_user_creation(self):
        user = self.create_user("randomName", "firstName", "lastName")
        self.assertTrue(isinstance(user, User))


    def test_employee_creation(self):
        employee = self.create_employee(helpers.generate_uuid(), "applicant266", "slackuser")
        self.assertTrue(isinstance(employee, Employee))
        self.assertEqual(employee.__str__(), employee.identifier)

    def test_menu_creation(self):
        date = datetime.now()
        menu = self.create_menu("testuser", "Test", "User", "Test Menu", date, datetime.now())
        self.assertTrue(isinstance(menu, Menu))

    def test_option_creation(self):
        menu = self.create_menu("testuser", "Test", "User", "Test Menu", datetime.now(), datetime.now())
        option = self.create_option(menu ,"Arroz", datetime.now(), datetime.now())
        self.assertTrue(isinstance(option, Option))
        self.assertEqual(option.__str__(), option.description)

    def test_order_creation(self):
        menu = self.create_menu("testuser", "Test", "User", "Test Menu", datetime.now(), datetime.now())
        option = self.create_option(menu ,"Arroz", datetime.now(), datetime.now())
        employee = self.create_employee(helpers.generate_uuid(), "applicant26dsa6", "slackuser")
        user_uuid = uuid.UUID(employee.identifier).hex

        order = self.create_order(menu, option, user_uuid, "any customization")

        self.assertTrue(isinstance(order, Order))
