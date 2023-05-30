from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    author = models.CharField(max_length=100, blank=False)
    year = models.IntegerField(blank=False, default=2000)