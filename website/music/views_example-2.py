from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(reqest):
    return HttpResponse("<h1> This is Music app home page. </h1>")

def detail(request, album_id):
    return HttpResponse("<h2> Details for Album id:" + str(album_id) +  "</h2>")