from django.shortcuts import render

app_name = 'appbib'

def Home(request):
    return render(request, 'appbib/home.html')
def Login(request):
    return render(request, 'appbib/login.html')
def singup(request):
    return render(request, 'appbib/singup.html')
def library(request):
    return render(request, 'appbib/library.html')
def book(request):
    return render(request, 'appbib/book.html')
def profil(request):
    return render(request, 'appbib/profil.html')  
def rent(request):
    return render(request, 'appbib/rent.html')            