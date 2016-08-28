# from django.contrib import admin
from django.conf.urls import url
from .views import index

urlpatterns = [
    url(r'^eCaretaker/', index, name='Home'),
]