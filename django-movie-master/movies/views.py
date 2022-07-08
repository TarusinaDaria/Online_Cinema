from django.shortcuts import render
from django.http import HttpResponseNotFound

# Create your views here.

from django.views.generic.base import View
from .forms import RatingForm, Rating   # , ReviewForm,


from django.http import HttpResponse
from .models import Movie


def index_page(request):
    movies = Movie.objects.all().order_by('kinopoisk_id')
    # movie_stars = Rating.objects.all().order_by('ip')
    return render(request, 'movies/index.html', {'movies' : movies})  # 'movie_stars' : movie_stars})


def player_page(request, kinopoisk_id):
    return render(request, 'movies/player.html', {'kinopoisk_id':kinopoisk_id})


def films_page(request):
    movies = Movie.objects.all().order_by('kinopoisk_id')
    return render(request, 'movies/films.html', {'movies' : movies})


def films_comedy_page(request):
    movies = Movie.objects.all().order_by('kinopoisk_id')
    return render(request, 'movies/films_comedy.html', {'movies' : movies})


def films_drama_page(request):
    movies = Movie.objects.all().order_by('kinopoisk_id')
    return render(request, 'movies/films_drama.html', {'movies' : movies})


def films_horror_page(request):
    movies = Movie.objects.all().order_by('kinopoisk_id')
    return render(request, 'movies/films_horror.html', {'movies' : movies})


def films_romance_page(request):
    movies = Movie.objects.all().order_by('kinopoisk_id')
    return render(request, 'movies/films_romance.html', {'movies' : movies})


def series_page(request):
    movies = Movie.objects.all().order_by('kinopoisk_id')
    return render(request, 'movies/series.html', {'movies' : movies})


def series_comedy_page(request):
    movies = Movie.objects.all().order_by('kinopoisk_id')
    return render(request, 'movies/series_comedy.html', {'movies' : movies})


def series_drama_page(request):
    movies = Movie.objects.all().order_by('kinopoisk_id')
    return render(request, 'movies/series_drama.html', {'movies' : movies})


def series_horror_page(request):
    movies = Movie.objects.all().order_by('kinopoisk_id')
    return render(request, 'movies/series_horror.html', {'movies' : movies})


def series_romance_page(request):
    movies = Movie.objects.all().order_by('kinopoisk_id')
    return render(request, 'movies/series_romance.html', {'movies' : movies})


def cartoons_page(request):
    movies = Movie.objects.all().order_by('kinopoisk_id')
    return render(request, 'movies/cartoons.html', {'movies' : movies})


def cartoons_science_fiction_page(request):
    movies = Movie.objects.all().order_by('kinopoisk_id')
    return render(request, 'movies/cartoons_science_fiction.html', {'movies' : movies})


def cartoons_mystery_page(request):
    movies = Movie.objects.all().order_by('kinopoisk_id')
    return render(request, 'movies/cartoons_mystery.html', {'movies' : movies})


def cartoons_anime_page(request):
    movies = Movie.objects.all().order_by('kinopoisk_id')
    return render(request, 'movies/cartoons_anime.html', {'movies' : movies})



def admin(request):
    return render(request, 'movies/admin.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


"""    Измениния   """
"""
class AddReview(View):
Отзывы

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
"""

class AddStarRating(View):
    """Добавление рейтинга фильму"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
