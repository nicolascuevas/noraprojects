# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from random import randint

from django.contrib.auth.models import User
from django.test import TestCase

from meals import helpers
from meals.models import Employee, Menu, Option, Order


# Create your tests here.


class ModelsTest(TestCase):
    def create_employee(self, identifier, email):
        return Employee.objects.create(identifier=identifier, email=email)

    def create_user(self, username="testuser", first_name="Test", last_name="User"):
        return User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_superuser=False,
            is_active=True,
            is_staff=False
        )

    def create_menu(self, username, first_name, last_name, title="Test Menu", send_notification=False,
                    created_at=datetime.now(), updated_at=datetime.now()):
        return Menu.objects.create(
            user=self.create_user(username, first_name, last_name),
            send=send_notification,
            created_at=created_at,
            updated_at=updated_at,
            title=title,
            uuid=helpers.generate_uuid()
        )

    def create_option(self, description, created_at, updated_at):
        return Option.objects.create(
            menu_id=randint(1, 100),
            description=description,
            created_at=created_at,
            updated_at=updated_at
        )

    def test_employee_creation(self):
        employee = self.create_employee("11111111-1", "applicant@cornershopapp.com")
        self.assertTrue(isinstance(employee, Employee))
        self.assertEqual(employee.__str__(), employee.email)

    def test_menu_creation(self):
        menu = self.create_menu("testuser", "Test", "User", "Test Menu", False, datetime.now(), datetime.now())
        self.assertTrue(isinstance(menu, Menu))
        self.assertEqual(menu.__str__(), False)

    """
        This test will fail before 11 AM CLT unless we mock datetime.now, but couldn't make the mock work :/
    """

    def test_can_choose_menu(self):
        menu = self.create_menu("testuser", "Test", "User", "Test Menu", False, datetime.now(), datetime.now())
        self.assertFalse(menu.can_choose_menu())

    def test_option_creation(self):
        option = self.create_option("Arroz", datetime.now(), datetime.now())

        self.assertTrue(isinstance(option, Option))
        self.assertEqual(option.__str__(), option.description)

    def test_order_creation(self):
        order = Order.objects.create(
            employee_identifier="11111111-1",
            option=randint(1, 100),
            menu_id=randint(1, 100),
            customization=None,
            created_at=datetime.now()
        )

        self.assertTrue(isinstance(order, Order))
        self.assertEqual(order.__str__(), order.employee_identifier)
