from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'index.html')
def bib(request):
    return render(request, 'biblio.html')