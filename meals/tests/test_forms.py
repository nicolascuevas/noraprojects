from unittest import TestCase
from datetime import datetime, timedelta
from meals.forms import OrderForm
from meals.models import Option, Menu, Order, Employee
from django.contrib.auth.models import User
import uuid


class FormsTest(TestCase):
    # def make_options(self, menu):
    #     return [
    #         Option(menu=menu, description="Option1"),
    #         Option(menu=menu, description="Option2"),
    #         Option(menu=menu, description="Option3")
    #     ]

    # def create_user(self):
    #     return User.objects.create(
    #                 username="testuser",
    #                 email="testuser@testdomain.com",
    #                 password="supersecret"
    #             )

    # def create_employee(self):
    #     return Employee.objects.create(
    #                 identifier=uuid.uuid4().hex
    #             )
    # def create_menu(self, user):
    #     date = datetime.now() + timedelta(1)
    #     date = date.date()
    #     return Menu.objects.create(
    #                 uuid=uuid.uuid4().hex,
    #                 date= date, 
    #                 title="test menu", 
    #                 user=user
    #             )

