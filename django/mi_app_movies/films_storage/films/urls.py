from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='home'),
    path('producers/<slug:slug_parameter>/',views.producer,name="producer")
]
