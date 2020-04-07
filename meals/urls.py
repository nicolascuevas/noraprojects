from django.conf.urls import url
from meals.views import *

urlpatterns = [
    # menu
    url(r'^$', ListMenu.as_view(), name='list_menu'),
    url(r'^meals/add/$', CreateMenu.as_view(), name='create_menu'),
    url(r'^meals/edit/(?P<pk>\d+)/$', UpdateMenu.as_view(), name='update_menu'),

    # options
    url(r'^meals/option/(?P<pk>[0-9]+)/$', ListOption.as_view(), name='list_option'),
    url(r'^meals/option/add/(?P<pk>[0-9]+)/$', CreateOption.as_view(), name='create_option'),
    url(r'^meals/option/edit/(?P<pk>[0-9]+)/$', UpdateOption.as_view(), name='update_option'),

    # orders
    url(r'^menu/(?P<uuid>[0-9a-f-]+)$', today_menu, name='today_menu'),
    url(r'^orders/(?P<pk>[0-9]+)/$', ListOrder.as_view(), name="list_order"),
]