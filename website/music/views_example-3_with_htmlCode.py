from django.shortcuts import render
from django.http import HttpResponse
# Import Album from models for conecting databasee
from .models import Album
# Create your views here.

def index(reqest):
    #return HttpResponse("<h1> This is Music app home page. </h1>")
    #Get the all objects from Album
    all_albums = Album.objects.all()
    #Create variable with name html and return that variable.
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse("<h2> Details for Album id:" + str(album_id) +  "</h2>")
