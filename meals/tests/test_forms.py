from unittest import TestCase

from meals.forms import OrderForm
from meals.models import Option


# class FormsTest(TestCase):
#     def make_options(self):
#         return [
#             Option(id=1, menu_id=1, description="Option1"),
#             Option(id=2, menu_id=2, description="Option2"),
#             Option(id=3, menu_id=3, description="Option3")
#         ]

#     def test_invalid_form(self):
#         data = {'title': '', 'body': ''}
#         form = OrderForm(data=data, *[], **{'options': []})
#         self.assertFalse(form.is_valid())

#     def test_valid_form_without_customization(self):
#         data = {
#             'employee_identifier': '11111111-1',
#             'option': 1,
#         }
#         options = self.make_options()
#         form = OrderForm(data=data, *[], **{'options': options})
#         self.assertTrue(form.is_valid())

#     def test_valid_form_with_customization(self):
#         data = {
#             'employee_identifier': '11111111-1',
#             'option': 1,
#             'customization': "My Customization"
#         }
#         options = self.make_options()
#         form = OrderForm(data=data, *[], **{'options': options})
#         self.assertTrue(form.is_valid())