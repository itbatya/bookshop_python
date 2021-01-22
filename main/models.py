from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
