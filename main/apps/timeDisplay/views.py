from django.shortcuts import render, redirect, HttpResponse
from time import localtime, strftime

# Create your views here.
def index(request):
    context = {
    'time': strftime('%b %d, %Y %I:%M %p', localtime())
    }
    return render(request, 'timeDisplay/index.html', context)
