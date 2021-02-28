from datetime import date

from django.db import models
from django.db.models import Model


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actor and Director"
        verbose_name_plural = "Actors and Directors"


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200, default='')
    description = models.TextField()
    poster = models.ImageField(upload_to="movies/")
    year = models.PositiveIntegerField(default=2021)
    country = models.CharField(max_length=100)
    directors = models.ManyToManyField(Actor, verbose_name="director", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="actors", related_name="film_actors")
    genres = models.ManyToManyField(Genre, verbose_name="genres")
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(default=0, help_text="specify the amount in dollars")
    feels_in_usa = models.PositiveIntegerField(default=0, help_text="specify the amount in dollars")
    fees_in_the_world = models.PositiveIntegerField(default=0, help_text="specify the amount in dollars")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE, null=True)
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class MovieShots(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie shot"
        verbose_name_plural = "Movie shots"


class RatingStar(models.Model):
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = " Rating Star"
        verbose_name_plural = "Rating Stars"


class Rating(models.Model):
    ip = models.CharField(max_length=10)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="star")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="movie")

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    parent = models.ForeignKey('self', verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
