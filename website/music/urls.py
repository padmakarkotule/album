from django.conf.urls import include, url
from . import views 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url('^$', views.index, name='index'),
]