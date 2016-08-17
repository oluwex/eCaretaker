from django.contrib.auth.views import login
from django.conf.urls import url
from .views import index, register

urlpatterns = [
    url(r'^$', index, name='Home'),
    url(r'^login/', login, name='login'),
    url(r'^register/', register, name='register')
]