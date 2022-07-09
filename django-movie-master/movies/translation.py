from modeltranslation.translator import register, TranslationOptions
from .models import MovieShots


@register(MovieShots)
class MovieShotsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')