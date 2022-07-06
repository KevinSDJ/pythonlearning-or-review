from django.shortcuts import render
from django.http import HttpResponse
from films.models import Film
import sqlite3
# Create your views here.


def index(request):
    d= Film.objects.all()
    return render(request,'index.html',context={
        "lista":d
    })
