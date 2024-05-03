from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.messages import error
from django.http import HttpResponseRedirect  # For profile update redirection
import django.db.utils

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        error_displayed = False  # Flag to track if an error has been displayed

        if form.is_valid():
            try:
                user = form.save(commit=False)
                password = form.cleaned_data['password1']
                user.set_password(password)
                user.save()
                
                messages.success(request, "Account created successfully. You can now login.")
                return redirect('login')
            except django.db.utils.IntegrityError as e:
                if not error_displayed:
                    if 'username' in str(e):
                        messages.error(request, "A user with that username already exists. Please choose a different username.")
                        error_displayed = True
                    
        else:
            for error in form.errors.values():
                if not error_displayed:
                    if 'password2' in error and 'password_mismatch' in error:
                        messages.error(request, "Your passwords don't match. Please try again.")
                        error_displayed = True
                    else:
                        messages.error(request, error)
                        error_displayed = True
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('biblio')
        else:
            # Handle login form validation errors
            pass
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def biblio(request):
    return render(request, 'biblio.html')

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

    return render(request, 'change_password.html', {'form': form})
