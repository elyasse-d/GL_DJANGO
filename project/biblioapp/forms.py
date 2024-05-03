from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']
'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modifier les widgets des champs de mot de passe comme vous le souhaitez

class CustomProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'phone_number', 'email', 'city', 'studies', 'major', 'profile_picture']
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            # Ajoutez d'autres widgets personnalisés au besoin
        }'''