from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.audioquiz,name='audioquiz'),
    path('results',views.results,name='results'),
    path('getquiz',views.getquiz,name='getquiz'),
]
