from django.conf.urls import include, url
from . import views 
from django.contrib import admin
from django.urls import path
from os import name

urlpatterns = [
    # Home page for /music app
    url('^$', views.index, name='index'),
    # /music with some id's. Example pass Album id.
    # Here r means Regular expression
    # Most of the time (90% of time) regular expression start with ^ to match starting of word.
    # ^$ means no match, simple blank line and used for home page.
    # url (r'^(>pMalbum_id))$'),
    
    # /music/712
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),   
]