from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_title = models.CharField(max_length = 100)
    movie_description = models.TextField()
    movie_release_date = models.DateField()
    movie_director = models.CharField(max_length = 100)

    def __str__(self):
        return self.movie_title
