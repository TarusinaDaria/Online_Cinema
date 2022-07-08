from django.contrib import admin

from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

# Register your models here.
from .models import Movie, Rating, RatingStar #, MovieShots
# from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "movie", "ip")

"""
@admin.register(MovieShots)
class MovieShotsAdmin(TranslationAdmin):
    Кадры из фильма
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"

"""

admin.site.register(RatingStar)
