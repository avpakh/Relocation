from django.conf.urls import patterns, url, include
from gismap.views import *


urlpatterns = [

 url(r'^map/',map_page),
]