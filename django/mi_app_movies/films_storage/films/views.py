from django.shortcuts import render
from django.http import HttpResponse
from films.models import Film,Productor
import sqlite3
import json
# Create your views here.

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        if col[0]== 'poster':
            d[col[0]]= 'media/'+row[idx]
        else:
            d[col[0]] = row[idx]
    return d

def ask(id):
    query=f"""SELECT mv.title,mv.poster FROM films_film as mv 
    INNER JOIN films_productor_films as f_to_p ON mv.id=f_to_p.film_id
    INNER JOIN films_productor as pr ON f_to_p.productor_id=pr.id
    where pr.lastName="{id}";
    """
    conn= sqlite3.connect('db.sqlite3')
    conn.row_factory=dict_factory
    cursor=conn.cursor()
    data= cursor.execute(query).fetchall()
    cursor.close()
    conn.close()
    return data

def index(request):
    d= Productor.objects.all()
    for el in d:
        print(el.image_photo.url)
    return render(request,'index.html',context={
        "lista":d
    })

def producer(request,slug_parameter):
    indent=slug_parameter.split('-')[1]
    data =ask(indent)
    s= []
    for i in data:
        w=Film.objects.get(title=i["title"])
        s.append(w)
    p=Productor.objects.get(lastName=indent) 
    return render(request,'producer.html',context={
        "list":s,
        "pr":p
    })
