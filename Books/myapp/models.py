from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    author = models.CharField(max_length=100, blank=False)
    year = models.IntegerField(blank=False, default=2000)
    picture = models.ImageField(max_length=255,upload_to='pictures/',null=True , blank= True)
    pdf = models.FileField(upload_to='pdf/',null= True,blank=True)   



class Users(models.Model):
    name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=100,blank=False)

