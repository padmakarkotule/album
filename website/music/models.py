from django.contrib.auth.models import Permission, User
from django.db import models
from django.template.defaultfilters import default


class Album(models.Model):
    #user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    #is_favorite = models.BooleanField(default=False)
    #This will specify what are the parameters are return when function executes.
    #In this example it's returing only album_title and artist when execute command to get all objects.
    #E.g. run command, python manage.py shell and, import music app and run command on shell as,
    #>>> Album.objects.all()
    #<QuerySet [<Album: Object>, <Album: Object>]>
    #It will only Alunm objects and nothing else. To get data you need to add following functions.
    #E.g. in models.py e.g. add following line

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10, default=None)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    #is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

    