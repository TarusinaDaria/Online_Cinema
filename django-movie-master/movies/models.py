from django.db import models





class Movie(models.Model):
    name = models.CharField("Имя фильма", max_length=250)
    description = models.TextField("Описание", max_length=5000)
    image = models.ImageField("Изображение", upload_to = 'movie')
    films = models.BooleanField("Фильм", default=False, help_text="Выберите жанр фильма, который добавляете на сайт")
    films_comedy = models.BooleanField("Жанр - комедия", default=False)
    films_drama = models.BooleanField("Жанр - драма", default=False)
    films_horror = models.BooleanField("Жанр - ужасы", default=False)
    films_romanse = models.BooleanField("Жанр - мелодрамма", default=False)

    series = models.BooleanField("Сериал", default=False, help_text="Выберите жанр сериала, который добавляете на сайт")
    series_comedy = models.BooleanField("Жанр - комедия", default=False)
    series_drama = models.BooleanField("Жанр - драма", default=False)
    series_horror = models.BooleanField("Жанр - ужасы", default=False)
    series_romance = models.BooleanField("Жанр - мелодрамма", default=False)
    cartoons = models.BooleanField("Мультфильм", default=False, help_text="Выберите жанр мультфильма,"
                                                                          " который добавляете на сайт")
    mystery = models.BooleanField("Жанр - мистика", default=False)
    science_fiction = models.BooleanField("Жанр - фантастика", default=False)
    anime = models.BooleanField("Жанр - аниме", default=False)
    kinopoisk_id = models.IntegerField(null=False)

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return self.name

class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

"""
class MovieShots(models.Model):
    Кадры из фильма
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"
"""


"""
class Reviews(models.Model):
    Отзывы
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
"""


