from django.contrib import admin
from django.urls import path
from .views import Home , bib, rent, LibraryView



urlpatterns = [
    path('home/', Home, name='home'),
    path('index/', bib, name='index'),
    path('rent/', rent, name='rent'), 
    path('library/', LibraryView.as_view(), name='library'),  # URL pour afficher tous les livres
    path('library/<str:category>/', LibraryView.as_view(), name='library_category'), # URL pour afficher tous les livres ont le genre = category


]