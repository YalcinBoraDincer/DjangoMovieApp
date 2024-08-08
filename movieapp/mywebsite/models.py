from django.db import models

# Create your models here.

class Comment(models.Model):
    movieID = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    comment_text = models.CharField(max_length=200)
    rating = models.IntegerField()
    def __str__(self):
        return f'{self.user_name} - {self.movie_id}'
    
