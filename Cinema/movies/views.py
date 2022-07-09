"""

from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')
"""


from django.shortcuts import render
from .models import Movie


def index_page(request):
    movies = Movie.objects.all().order_by('name')
    return render(request, 'movies/index.html', {'movies': movies})


def player_page(request, kinopoisk_id):
    name = "g"  # надо подумать как это лучше сделать (как можно передать имя и потом не проходить по всем объектам в поисках нужного имени)
    return render(request, 'movies/player.html', {'kinopoisk_id': kinopoisk_id, 'names': name})


# def player_page(request, kinopoisk_id, name):
#     return render(request, 'movies/player.html', {'kinopoisk_id': kinopoisk_id, 'name': name}) в urls надо еще менять и разбираться как

