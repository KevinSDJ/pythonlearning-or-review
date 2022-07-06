from django.db import models
import datetime
import uuid
import os
from pathlib import Path

BASE_DIR= Path(__file__).resolve().parent.parent
# Create your models here.
dateNow= datetime.datetime.now()
class Genre(models.Model):
    id= models.UUIDField(default=uuid.uuid4,primary_key=True)
    name=models.CharField(max_length=64,null=False,unique=True)
    createDT=models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Film(models.Model):
    id= models.UUIDField(default=uuid.uuid4,primary_key=True)
    title= models.CharField(max_length=64,null=False,unique=True)
    sinopsis= models.TextField(max_length=400,null=False)
    poster= models.ImageField(null=True,blank=True,upload_to='imagenes')
    genres=models.ManyToManyField(Genre)
    createDT=models.DateField(auto_now=True)
    def __str__(self):
        return self.title

class Productor(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    firstName= models.CharField(max_length=64)
    image_photo=models.ImageField(upload_to='imagenes',null=True,blank=True)
    lastName= models.CharField(max_length=64,null=False)
    data_birth= models.DateField(null=True)
    films= models.ManyToManyField(Film)
    createDT= models.CharField(max_length=32,default=dateNow)
    def __str__(self):
        return self.lastName


