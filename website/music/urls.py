from django.conf.urls import include, url
from . import views 
from django.contrib import admin
from django.urls import path
from os import name

app_name = 'music'
urlpatterns = [
    # Home page for /music app
    url('^$', views.IndexView.as_view(), name='index'),
    # /music with some id's. Example pass Album id.
    # Here r means Regular expression
    # Most of the time (90% of time) regular expression start with ^ to match starting of word.
    # ^$ means no match, simple blank line and used for home page.
    # url (r'^(>pMalbum_id))$'),
    
    # /music/<album_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
    # url is /music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    
     # url is /music/album/2 (update pk e.g. 2)
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    
     # url is /music/2/delete  (delete pk)
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    
]