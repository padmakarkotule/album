from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
# Import template loader 
from django.shortcuts import render
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
    context = {'all_albums': all_albums} 
    #Following line renders, index.html and pass context (passes dictionary data) . 
    #return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', context)
    #Instead of context you can directly write code e.g. {'all_albums': all_albums}
    #E.g. return render(request, 'music/index.html', {'all_albums': all_albums}  )
def detail(request, album_id):
    #Example of Http404 Error
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404(" Album does not exit")
    return render(request, 'music/detail.html', {'album': album})
