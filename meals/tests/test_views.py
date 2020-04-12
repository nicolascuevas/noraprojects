from datetime import datetime, timedelta
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase, Client
from meals.models import Menu, Order, Option, Employee
import json
import uuid
from meals import helpers
from meals.views import ListMenu


class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.uuid_1 = uuid.uuid4().hex
        self.list_order_url = reverse("meals:list_menu")
        self.create_menu_url = reverse("meals:create_menu")
        self.update_menu_url = reverse("meals:update_menu", args=['1'])
        self.list_option_url = reverse("meals:list_option", args=['1'])
        self.create_option_url = reverse("meals:create_option", args=['1'])
        self.update_option_url = reverse("meals:update_option", args=['1'])
        self.create_order_url = reverse("meals:today_menu2", args=[self.uuid_1])
        self.show_order_url = reverse("meals:selected_menu", args=[self.uuid_1])
        self.edit_order_url = reverse("meals:edit_menu", args=['1'])

        self.user = User.objects.create(
            username="testuser",
            email="testuser@testdomain.com",
            password="supersecret"
        )
        self.client.login(username="testuser", password="supersecret")
        self.client.force_login(self.user)
        # 1 day in future
        self.date = datetime.now() + timedelta(1)
        self.date = self.date.date()
        self.menu_1 = Menu.objects.create(uuid=self.uuid_1 ,date= self.date, title="test menu", user=self.user )
        self.option_1_menu_1 = Option.objects.create(menu=self.menu_1, description="meal 1 Test" )
        self.option_2_menu_1 = Option.objects.create(menu=self.menu_1, description="meal 2 Test" )
        self.employee = Employee.objects.create(identifier=uuid.uuid4().hex)
        self.order_1 = Order.objects.create( menu=self.menu_1, employee=self.employee, option=self.option_1_menu_1, customization="customization text" )




    def test_view_list_menu(self):
        response = self.client.get(self.create_menu_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menu_add.html")

    def test_view_create_menu(self):

        response = self.client.get(self.update_menu_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menu_add.html")

    def test_view_create_menu(self):
        response = self.client.get(self.update_menu_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menu_add.html")

    def test_view_create_menu_POST(self):
        #5 dias in future
        date = datetime.now() + timedelta(5)
        date = date.date()
        response = self.client.post( self.create_menu_url, {
            'title': "menu_title",
            'date': date
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Menu.objects.all().last().date, date)
        self.assertEquals(Menu.objects.all().last().title, "menu_title")

    def test_view_update_menu_POST(self):
        #5 dias in future
        date = datetime.now() + timedelta(5)
        date = date.date()
        menu = Menu.objects.create(title="menu_title", date=date, user=self.user)

        response = self.client.post( reverse("meals:update_menu", kwargs={'pk': menu.id}), {
            'title': "menu_title_updated",
            'date': date
        })
        latest_menu = Menu.objects.all().last()
        self.assertEquals(response.status_code, 302)
        self.assertEquals(latest_menu.uuid, menu.uuid)
        self.assertEquals(latest_menu.title, "menu_title_updated")


    def test_view_list_option(self):
        response = self.client.get(self.list_option_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menu_option.html")

    def test_view_create_option(self):
        response = self.client.get(self.create_option_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menu_option_add.html")

    def test_view_create_option_POST(self):
        
        response = self.client.post(self.create_option_url, {
            'menu': self.menu_1,
            'description': "New option"
        })
        option = Option.objects.all().last()
        self.assertEquals(response.status_code, 302)
        self.assertEquals(option.description, "New option")
        self.assertEquals(option.menu, self.menu_1)


    def test_view_update_option(self):
        response = self.client.get(self.update_option_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menu_option_add.html")

    def test_view_update_option_POST(self):
        option_test = Option.objects.create(menu=self.menu_1, description="New Option")

        response = self.client.post(reverse("meals:update_option", kwargs={'pk':option_test.id}), {
            'id': option_test.id,
            'description': "Updated Option"
        })

        option = Option.objects.all().last()
        self.assertEquals(response.status_code, 302)
        self.assertEquals(option.description, "Updated Option")
        self.assertEquals(option.id, option_test.id)


    def test_view_create_order(self):
        response = self.client.get(self.create_order_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "meals/employee_meal_choose.html")

    def test_view_show_order_without_seession(self):
        response = self.client.get(self.show_order_url)
        self.assertEquals(response.status_code, 404)

    def test_view_show_order_with_seession(self):
        #set employee session to identify employee
        session = self.client.session
        session['employee_token'] = self.employee.identifier
        session.save()
        response = self.client.get(self.show_order_url)
        self.assertEquals(response.status_code, 200)

    def test_view_edit_order_without_seession(self):
        #set employee session to identify employee
        response = self.client.get(self.edit_order_url)
        self.assertEquals(response.status_code, 404)

    def test_view_edit_order_with_seession(self):
        session = self.client.session
        session['employee_token'] = self.employee.identifier
        session.save()
        response = self.client.get(self.edit_order_url)
        self.assertEquals(response.status_code, 200)


    def test_view_create_valid_menu_order_with_seession(self):
        #different employee to allow his answer
        employee = Employee.objects.create(identifier=uuid.uuid4().hex)
        session = self.client.session
        session['employee_token'] = employee.identifier
        session.save()
        response = self.client.post(self.create_order_url, {
            'option': self.option_1_menu_1.id,
            'customization': "Custom Menu ber8pybq"
        })
        order = Order.objects.all().last()
        self.assertEquals(response.status_code, 302)
        self.assertEquals(order.customization, "Custom Menu ber8pybq")

    def test_view_create_valid_menu_order_without_seession(self):
        session = self.client.session
        session['employee_token'] = None
        session.save()

        response = self.client.post(self.create_order_url, {
            'option': self.option_1_menu_1.id,
            'customization': "Custom Menu ber8pybq"
        })
        order = Order.objects.all().last()
        self.assertEquals(response.status_code, 404)

    def test_view_create_invalid_employee_uuid_menu_order_with_seession(self):
        session = self.client.session
        session['employee_token'] = uuid.uuid4().hex
        session.save()
        response = self.client.post(self.create_order_url, {
            'option': self.option_1_menu_1.id,
            'customization': "Custom Menu ber8pybq"
        })
        order = Order.objects.all().last()
        self.assertEquals(response.status_code, 404)

    def test_view_create_old_menu_order_with_seession(self):
        #different employee to allow his answer
        session = self.client.session
        session['employee_token'] = self.employee.identifier
        session.save()
        # 1 day in past
        date = datetime.now() + timedelta(2)
        date = date.date()
        menu = Menu.objects.create( title="new title", date=date, user=self.user )
        option = Option.objects.create(menu=menu, description="New option")

        response = self.client.post(reverse("meals:today_menu2", kwargs={'uuid':menu.uuid}), {
            'option': option.id,
            'customization': "Custom Menu bvenqrugcdw438"
        })

        order = Order.objects.all().last()
        self.assertEquals(response.status_code, 302)

    def test_view_update_valid_menu_order_with_session(self):
        session = self.client.session
        session['employee_token'] = self.employee.identifier
        session.save()

        response = self.client.post(reverse("meals:edit_menu", kwargs={'pk':'1'}), {
            'option': self.option_2_menu_1.id,
            'customization': "Custom Menu 2",
            'id': self.order_1.id,
        })
        order =  Order.objects.all().last()
        self.assertEquals(response.status_code, 302)
        self.assertEquals(order.customization, "Custom Menu 2")
        self.assertEquals(order.option, self.option_2_menu_1)

