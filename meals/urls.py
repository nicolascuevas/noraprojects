from django.conf.urls import url
from meals.views import *

urlpatterns = [
    # menu
    url(r'^$', ListMenu.as_view(), name='list_menu'),
    url(r'^add/$', CreateMenu.as_view(), name='create_menu'),
    url(r'^edit/(?P<pk>\d+)/$', UpdateMenu.as_view(), name='update_menu'),

    # options
    url(r'^option/(?P<pk>[0-9]+)/$', ListOption.as_view(), name='list_option'),
    url(r'^option/add/(?P<pk>[0-9]+)/$', CreateOption.as_view(), name='create_option'),
    url(r'^option/edit/(?P<pk>[0-9]+)/$', UpdateOption.as_view(), name='update_option'),

    url(r'^orders/(?P<pk>[0-9]+)/$', ListOrder.as_view(), name="list_order"),

]