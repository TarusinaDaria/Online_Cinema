from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index_page, name='home'),
    path('movie/<int:kinopoisk_id>', views.player_page),
    path('films', views.films_page, name='films'),
    path('series', views.series_page, name='series'),
    path('admin', views.admin, name='admin'),
]
