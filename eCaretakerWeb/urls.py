# from django.contrib import admin
from django.conf.urls import url
from .views import index, register, loguserin, logoff

urlpatterns = [
    url(r'^$', index, name='Home'),
    url(r'^login/', loguserin, name='login'),
    url(r'^register/', register, name='register'),
    url(r'^logoff/', logoff, name='logoff'),
]