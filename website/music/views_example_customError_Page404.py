from django.shortcuts import render, get_object_or_404, render_to_response
#from django.http import HttpResponse
# Import template loader 
# Import Album from models for conecting databasee
from .models import Album, Song
from django.template import RequestContext

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
    #album = Album.objects.get(pk=album_id)
    try:  
        album = get_object_or_404(Album, pk=album_id)     
    
        return render(request, 'music/detail.html', {'album': album})
    except Exception as e:
        return render(request, 'music/404.html')
        
        
def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You didn't selected valid song",
            })
    else:
        selected_song.is_favorite = True
        selected_song.save()
    return render(request, 'music/detail.html', {'album': album})

# --------------------Error handling------------------#############
#def custom_404(request):
#    return render(request, 'musci/404.html', {}, status=404)

def handler404(request):
    #response = render_to_response('music/404.html')
    #response.status_code = 404
    #return response
    return render(request, 'music/404.html')


def handler500(request):
    #response = render_to_response('music/500.html') 
    #response.status_code = 500
    #return response
    return render(request, 'music/500.html')
