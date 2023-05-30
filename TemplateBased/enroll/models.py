from django.db import models

# Create your models here.

class Games(models.Model):
    Game_Name = models.CharField(max_length=200)
    Ratings = models.FloatField()
    Year_Of_Release = models.IntegerField()
    Price = models.IntegerField()
    