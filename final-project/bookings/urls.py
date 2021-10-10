from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('blind',views.blind,name="blind"),
    path('helper',views.helper,name="helper"),
    path('profile/<str:profileuser>',views.profile,name="profile"),
    path('togglebool',views.togglebool,name="togglebool"),
]
