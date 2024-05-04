from django.shortcuts import render

app_name = 'appbib'

def Home(request):
    return render(request, 'appbib/home.html')