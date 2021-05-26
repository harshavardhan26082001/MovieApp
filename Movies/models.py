from django.db import models


class Movies(models.Model):
    movie_name = models.CharField(max_length=500)
    movie_id = models.IntegerField()
    release_date = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField()
    movie_genre = models.TextField(max_length=10000, null=True, blank=True)
    movie_popularity = models.CharField(max_length=100, null=True, blank=True)
    movie_rating = models.CharField(max_length=100, null=True, blank=True)
    movie_trailer = models.CharField(max_length=5000, null=True, blank=True)
    storyline = models.TextField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    movie_director = models.CharField(max_length=200, null=True, blank=True)
    movie_actor1 = models.CharField(max_length=1000, null=True, blank=True)
    movie_actor2 = models.CharField(max_length=100, null=True, blank=True)
    movie_actor3 = models.CharField(max_length=100, null=True, blank=True)
    movie_actor4 = models.CharField(max_length=100, null=True, blank=True)
