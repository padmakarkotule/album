from django.shortcuts import render
from django.http import HttpResponse
# Import template loader 
from django.template import loader
# Import Album from models for conecting databasee
from .models import Album
# Create your views here.

def index(request):
    #return HttpResponse("<h1> This is Music app home page. </h1>")
    #Get the all objects from Album
    all_albums = Album.objects.all()
    #Create variable with name html and return that variable.
    
    #In following you don't need to give directory name as templates, as it's already taken care
    #by django framework, so don't need to give path such as, 'templates/music/index.html'
    template = loader.get_template('music/index.html')
    context = {
            'all_albums': all_albums,       
        } 
    #Following line renders, index.html and pass context (passes dictionary data) . 
    return HttpResponse(template.render(context, request))

def detail(request, album_id):
    return HttpResponse("<h2> Details for Album id:" + str(album_id) +  "</h2>")
