from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    lista=["s","d","9","seew",2,"dsad","dsda","dsada"]
    return render(request,'index.html',context={
        "lista":lista
    })
