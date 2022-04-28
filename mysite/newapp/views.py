from django.shortcuts import render
from .models import Movies

# Create your views here.

def movie_list(request):
    movie_object = Movies.objects.all()