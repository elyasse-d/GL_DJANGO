from django.contrib import admin
from django.urls import path
from .views import Home , CustomLoginView ,singup , library ,book,profil ,rent , search_results ,confirm_rent ,error,edit_profile,validate_returned_books ,returned_books
from django.contrib.auth import views as auth_view
from .forms import LoginForm


urlpatterns = [
    path('', Home, name='home'),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('singup/', singup, name='singup'),
    path('book/<int:pk>/', book, name='book'),
    path('profil/', profil, name='profil'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('rent/<int:book_id>/', rent, name='rent'),
    path('logout/', auth_view.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('library/', library, name='library'),
    path('search/', search_results, name='search_results'),
    path('confirm/<int:book_id>/', confirm_rent, name='confirm_rent'),
    path('error', error , name='error'),
    path('valid/', validate_returned_books, name='valid'),
    path('returned/', returned_books, name='returned'),
    
    
]