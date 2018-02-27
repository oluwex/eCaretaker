from django.conf.urls import url
from .views import register, loguserin, logoff, index, profile

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', loguserin, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^logoff/$', logoff, name='logoff'),
    # url(r'^profile/$', profile, name='profile'),
    url(r'(?P<username>\w+)/profile/$', profile, name='profile')
]