from django.conf.urls import url
from django.conf.urls.static import static
from .views import *

app_name='directory'
urlpatterns = [
    url(r'^$',home, name='home'),
   # url(r'^sortby=(?P<sorting_string>[-a-z&_]+)$',index, name='index'),
    url(r'^\?&page=(?P<page>\d+)$',index, name='index'),
    url(r'^\?sortby=(?P<sorting_string>-?name)(&page=(?P<page>\d+))?$',index, name='index'),
    url(r'^\?sortby=(?P<sorting_string>-?industries)(&page=(?P<page>\d+))?$',index, name='index'),
    url(r'^\?sortby=(?P<sorting_string>-?year_founded)(&page=(?P<page>\d+))?$',index, name='index'),
    url(r'^\?sortby=(?P<sorting_string>-?stage)(&page=(?P<page>\d+))?$',index, name='index'),
    url(r'^\?sortby=(?P<sorting_string>-?funding)(&page=(?P<page>\d+))?$',index, name='index'),
    url('^profile/(?P<company_id>\d+)$', profile),
]
