from django.views import View
from .models import Book , BorrowHistory
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm
from .forms import CustomUserCreationForm ,ProfileEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.messages import error
from django.http import HttpResponseRedirect  # For profile update redirection
import django.db.utils
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from .forms import LoginForm , ProfileEditForm
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from datetime import timedelta
from django.contrib.auth import login
from .models import CustomUser
from .models import Profile , ReturnedBook


app_name = 'appbib'

def Home(request):
    return render(request, 'appbib/home.html')
def Login(request):
    return render(request, 'appbib/login.html')
def book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'appbib/book.html', {'book': book})
@login_required
def profil(request):
    user = request.user
    profile = user.profile  # Assuming a OneToOne relation with the user as you've defined
    rented_books = user.borrowed_books.all()
    return render(request, 'appbib/profil.html', {
        'profile': profile,
        'rented_books': rented_books
    })
from .forms import ProfileEditForm

@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile, user=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated.')
            # Render the same page with a success message
            return render(request, 'appbib/edit_profile.html', {'form': form,'profile': profile })
        else:
            # If the form is not valid, render the page with error messages
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileEditForm(instance=profile, user=user)

    return render(request, 'appbib/edit_profile.html', {'form': form , 'profile': profile })

def error(request):
    return render(request, 'appbib/error.html')
      
      
def singup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Create a profile with default values
            Profile.objects.create(
                user=user,
                profile_picture='appbib/avatar.jpeg',  # Provide the path to your default profile picture  
                birthdate=timezone.now(),  
                name=user.username  
            )
            return redirect('library')  # Redirect to the library page after successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'appbib/sigup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'appbib/login.html'
    authentication_form = LoginForm
    success_url = reverse_lazy('library') 

    @method_decorator(user_passes_test(lambda u: not u.is_authenticated, login_url='library'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

def change_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = get_user_model().objects.filter(email=email).first()

            if user:
                messages.warning(request, "An email for password reset has already been sent to this email address.")
                return redirect('change_password')
            else:
                messages.error(request, "The email address you entered is not associated with any account.")
                return redirect('change_password')

    else:
        form = PasswordResetForm() 

    return render(request, 'home.html', {'form': form})

def library(request):
    books = Book.objects.all()

    # Get distinct genres and languages
    genres = set(Book.objects.values_list('genre', flat=True))
    languages = set(Book.objects.values_list('language', flat=True))

    selected_genres = request.GET.getlist('genre')
    selected_languages = request.GET.getlist('language')

    if selected_genres:
        books = books.filter(genre__in=selected_genres)

    if selected_languages:
        books = books.filter(language__in=selected_languages)

    return render(request, 'appbib/library.html', {
        'books': books,
        'genres': genres,
        'languages': languages,
        'selected_genres': selected_genres,
        'selected_languages': selected_languages,
    })

def search_results(request):
    query = request.GET.get('q')
    # Perform search logic here, for example:
    books = Book.objects.filter(title__icontains=query)
    genres = Book.objects.values_list('genre', flat=True).distinct()
    languages = Book.objects.values_list('language', flat=True).distinct()

    selected_genres = request.GET.getlist('genre')
    selected_languages = request.GET.getlist('language')

    if selected_genres:
        books = books.filter(genre__in=selected_genres,title__icontains=query)

    if selected_languages:
        books = books.filter(language__in=selected_languages,title__icontains=query)
    return render(request, 'appbib/library.html', {'books': books, 'query': query ,
        'genres': genres,
        'languages': languages,
        'selected_genres': selected_genres,
        'selected_languages': selected_languages,})



@login_required
def rent(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user = request.user
    
    # Check if the book is available
    if not book.is_available():
        message = "Sorry, this book is currently unavailable."
    # Check if the user has rented the book in the past 15 days
    elif BorrowHistory.objects.filter(book=book, user=user, date_borrowed__gte=timezone.now() - timedelta(days=15)).exists():
        message = "You have already rented this book in the past 15 days."
    else:
        message = None
    
    context = {
        'book': book,
        'user': user,
        'message': message
    }
    return render(request, 'appbib/rent.html', context)

@login_required
def confirm_rent(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user = request.user
    
    # Check if the book is available
    if not book.is_available():
        messages.error(request, "Sorry, this book is currently unavailable.")
        return render(request, 'appbib/error.html')  # Render error page
    # Check if the user has rented the book in the past 15 days
    elif BorrowHistory.objects.filter(book=book, user=user, date_borrowed__gte=timezone.now() - timedelta(days=15)).exists():
        messages.error(request, "You have already rented this book in the past 15 days.")
        return render(request, 'appbib/error.html')  # Render error page
    else:
        # Proceed to rent the book
        book.quantity -= 1
        book.save()
        BorrowHistory.objects.create(
            user=user,
            book=book,
            date_borrowed=timezone.now(),
            date_returned=timezone.now() + timedelta(days=15),
        )
        # Add success message
        messages.success(request, "You have successfully rented the book.")
        # Render the book page with the success message
        return render(request, 'appbib/book.html', {'book': book, 'message': 'You have successfully rented the book.'})

def returned_books(request):
    returned_books = ReturnedBook.objects.all()
    if request.method == 'POST':
        returned_book_id = request.POST.get('returned_book_id')
        returned_book = ReturnedBook.objects.get(id=returned_book_id)
        returned_book.validated = True
        returned_book.save()
        return redirect('returned')
    return render(request, 'appbib/returned_books.html', {'returned_books': returned_books})

def validate_returned_books(request):
    # Filter BorrowHistory to get returned books
    returned_books = BorrowHistory.objects.filter(returned=True)

    # Update quantity of each book
    for history in returned_books:
        book = history.book
        book.quantity = F('quantity') + 1  # Increment quantity by 1
        book.save()

    # Optionally, you can delete the entries from BorrowHistory for validated books
    returned_books.delete()

    return HttpResponse("Returned books validated successfully.")