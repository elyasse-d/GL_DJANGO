from django.shortcuts import render
from django.views import View
from .models import Book


# Create your views here.

def Home(request):
    return render(request, 'home.html')

def rent(request):
    return render(request, 'rent.html')

def bib(request):
    return render(request, 'biblio.html')

# Get Library starts here : 
class LibraryView(View):
    def get(self, request, category=None):
        
        if category:           # Récupérer les livres selon la catégorie donnée
            books = Book.objects.filter(genre=category)
        else:
            books = Book.objects.all()
        return render(request, "app/library.html", {"books": books})

# Fin de Get Library 


