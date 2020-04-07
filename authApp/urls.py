from django.contrib.auth.views import logout_then_login
from django.conf.urls import url
from . import views

app_name = 'authApp'

urlpatterns = [
    url(r'^signup/$', views.RegisterView.as_view(), name='signup'),
    url(r'^login/$', views.LoginTemplateView.as_view(), name='login'),
    url(r'^logout$', logout_then_login, name='logout'),
]
