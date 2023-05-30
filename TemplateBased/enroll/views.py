from django.shortcuts import render , redirect
from .models import Games

# Create your views here.
def getGames(request):
    obj = Games.objects.all()
    return render (request, "game-list.html",{'books':obj})