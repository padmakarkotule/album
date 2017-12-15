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


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10, default=None)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    #is_favorite = models.BooleanField(default=False)


    