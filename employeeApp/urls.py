from django.conf.urls import url
from employeeApp.views import *

urlpatterns = [

    url(r'^menu/(?P<user_uuid>[0-9a-f-]+)$', employee_meal_choose, name='employee_meal_choose'),
    url(r'^menu2/(?P<uuid>[0-9a-f-]+)$', today_menu, name='today_menu'),
]