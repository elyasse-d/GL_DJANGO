from django.contrib import admin
from django.urls import path
from .views import Home , bib



urlpatterns = [
    path('home/', Home, name='home'),
    path('index/', bib, name='index'),
]