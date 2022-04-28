from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

# Create your views here.

def movie_list(request):
    movie_object = Movies.objects.all()

    paginator = Paginator(movie_object, 4)
    page = request.GET.get('page')
    movie_object = paginator.get_page(page)

    return render(request, 'newapp/movies_list.html', {'movie_object':movie_object})