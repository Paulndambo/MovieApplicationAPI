from turtle import title
from django.db import models

# Create your models here.
MOVIE_TYPES = (
    ("movie", "movie"),
    ("series", "series"),
    ("episode", "episode"),
)

class Movie(models.Model):
    title = models.CharField(max_length=500)
    year = models.CharField(max_length=20, null=True)
    rated = models.CharField(max_length=20, null=True)
    released = models.CharField(max_length=50, null=True)
    runtime = models.CharField(max_length=200, null=True)
    genre = models.TextField(null=True)
    actors = models.TextField(null=True)
    writer = models.TextField(null=True)
    director = models.CharField(max_length=200, null=True)
    plot = models.TextField(null=True)
    language = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=200, null=True)
    awards = models.TextField(null=True)
    poster = models.CharField(max_length=200, null=True)
    ratings = models.JSONField(null=True)
    metascore = models.CharField(max_length=20, null=True)
    imdb_rating = models.CharField(max_length=20, null=True)
    imdb_votes = models.CharField(max_length=20, null=True)
    imdb_id = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, choices=MOVIE_TYPES, null=True)
    total_seasons = models.IntegerField(default=0)
    response = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie.title

    @property
    def movie_title(self):
        return self.movie.title