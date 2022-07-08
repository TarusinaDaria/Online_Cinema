from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index_page, name='home'),
    path('movie/<int:kinopoisk_id>', views.player_page),
    path('films', views.films_page, name='films'),
    path('films/comedy', views.films_comedy_page, name='films_comedy'),
    path('films/drama', views.films_drama_page, name='films_drama'),
    path('films/horror', views.films_horror_page, name='films_horror'),
    path('films/romance', views.films_romance_page, name='films_romance'),
    path('series/comedy', views.series_comedy_page, name='series_comedy'),
    path('series/drama', views.series_drama_page, name='series_drama'),
    path('series/horror', views.series_horror_page, name='series_horror'),
    path('series/romance', views.series_romance_page, name='series_romance'),
    path('cartoons/mystery', views.cartoons_mystery_page, name='cartoons_mystery'),
    path('cartoons/anime', views.cartoons_anime_page, name='anime_drama'),
    path('cartoons/science_fiction', views.cartoons_science_fiction_page, name='cartoons_science_fiction'),
    path('series', views.series_page, name='series'),
    path('cartoons', views.cartoons_page, name='cartoons'),
    path('admin', views.admin, name='admin'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
]
