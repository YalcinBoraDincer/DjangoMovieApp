from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200)
    imdb_id = models.CharField(max_length=50, unique=True)
    poster_url = models.URLField(max_length=500, blank=True, null=True)
    # Diğer gerekli alanlar

    def __str__(self):
        return self.title

class Comment(models.Model):
    #movie_id = models.IntegerField(default=0)  # Yeni eklenen alan
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.rating}'
