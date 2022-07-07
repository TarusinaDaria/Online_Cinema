from django.shortcuts import render
from django.http import HttpResponseNotFound

# Create your views here.
from django.http import HttpResponse
from .models import Movie


def index_page(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies' : movies})


def player_page(request, kinopoisk_id):
    return render(request, 'movies/player.html', {'kinopoisk_id':kinopoisk_id})


def films_page(request):
    movies = Movie.objects.all()
    return render(request, 'movies/films.html', {'movies' : movies})


def series_page(request):
    movies = Movie.objects.all()
    return render(request, 'movies/series.html', {'movies' : movies})


def admin(request):
    return render(request, 'movies/admin.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
