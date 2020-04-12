from datetime import datetime

from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase

from meals import helpers
from meals.models import Menu
from meals.views import ListMenu


# class ViewsTest(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         cls.factory = RequestFactory()
#         cls.user = User.objects.create(
#             username="testuser",
#             email="testuser@testdomain.com",
#             password="supersecret"
#         )
#         Menu.objects.create(
#             id=1,
#             user=cls.user,
#             date=datetime.now(),
#             created_at=datetime.now(),
#             updated_at=datetime.now(),
#             title="Test Menu 1",
#         )


#     def test_home(self):
#         request = self.factory.get("")
#         request.user = self.user

#         response = ListMenu.as_view()(request)

#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Create new menu")
#         self.assertContains(response, "Title")
#         self.assertContains(response, "Menu")

