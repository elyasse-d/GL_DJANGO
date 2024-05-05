from django.contrib import admin
from django.urls import path
from .views import Home , Login ,singup , library ,book,profil ,rent



urlpatterns = [
    path('', Home, name='home'),
    path("login/", Login, name="login"),
    path('singup/', singup, name='singup'),
    path('library/', library, name='library'),
    path('book/', book, name='book'),
    path('profil/', profil, name='profil'),
    path('rent/', rent, name='rent'),

]