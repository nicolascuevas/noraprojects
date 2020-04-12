from django.conf.urls import url
from meals.views import *

urlpatterns = [

    url(r'^$', ListMenu.as_view(), name='list_menu'),
    # menu
    url(r'^meals/$', ListMenu.as_view(), name='list_menu'),
    url(r'^meals/add/$', CreateMenu.as_view(), name='create_menu'),
    url(r'^meals/edit/(?P<pk>\d+)/$', UpdateMenu.as_view(), name='update_menu'),

    # options
    url(r'^meals/option/(?P<pk>[0-9]+)/$', ListOption.as_view(), name='list_option'),
    url(r'^meals/option/add/(?P<pk>[0-9]+)/$', CreateOption.as_view(), name='create_option'),
    url(r'^meals/option/edit/(?P<pk>[0-9]+)/$', UpdateOption.as_view(), name='update_option'),

    url(r'^orders/(?P<pk>[0-9]+)/$', ListOrder.as_view(), name="list_order"),

    url(r'^menu/(?P<uuid>[0-9a-f-]+)$', CreateOrder.as_view(), name='today_menu2'),
    url(r'^menu/(?P<uuid>[0-9a-f-]+)/show$', today_menu_show, name='selected_menu'),
    url(r'^menu/edit/(?P<pk>\d+)$', UpdateOrder.as_view(), name='edit_menu'),




]