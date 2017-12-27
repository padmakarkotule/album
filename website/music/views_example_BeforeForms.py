from django.views import generic
from .models import Album

class IndexView(generic.ListView):
    #Define which index file you want to use to show the pages.
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'
