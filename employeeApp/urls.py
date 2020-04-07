from django.conf.urls import url
from meals.views import *

urlpatterns = [

    url(r'^menu/(?P<uuid>[0-9a-f-]+)$', today_menu, name='today_menu'),
]