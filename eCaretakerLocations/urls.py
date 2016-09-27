from django.conf.urls import url
from .views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'(?P<type>\w+)/$', search, name='search')
]