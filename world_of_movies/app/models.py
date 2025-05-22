from django.db import models

class Movie(models.Model):
    cover = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    rating = models.FloatField()

    def __str__(self):
        return f"{self.title} - {self.director}"