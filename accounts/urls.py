from django.conf.urls import url
from .views import register, loguserin, logoff, index

urlpatterns = [
    url(r'^', index, name='index'),
    url(r'^login/$', loguserin, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^logoff/$', logoff, name='logoff'),
]