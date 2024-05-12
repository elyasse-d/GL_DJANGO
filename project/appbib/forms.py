from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UsernameField , PasswordChangeForm , SetPasswordForm, PasswordResetForm
from .models import CustomUser
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus ':'True','class':'text-iwhite w-full px-4 py-2 bg-iblack  border-b-2 border-b-gray-500 focus:outline-none font-helvetica-ultra-light','placeholder':'password'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'text-iwhite w-full px-4 py-2 bg-iblack  border-b-2 border-b-gray-500 focus:outline-none font-helvetica-ultra-light','placeholder':'password'}))


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'password1', 'password2']

class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'text-iwhite w-full px-4 py-2 bg-iblack  border-b-2 border-b-gray-500 focus:outline-none font-helvetica-ultra-light'
    }))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'text-iwhite w-full px-4 py-2 bg-iblack  border-b-2 border-b-gray-500 focus:outline-none font-helvetica-ultra-light'
    }))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={
        'class': 'text-iwhite w-full px-4 py-2 bg-iblack  border-b-2 border-b-gray-500 focus:outline-none font-helvetica-ultra-light'
    }))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'text-iwhite w-full px-4 py-2 bg-iblack  border-b-2 border-b-gray-500 focus:outline-none font-helvetica-ultra-light'
    }))
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={
        'class': 'text-iwhite w-full px-4 py-2 bg-iblack  border-b-2 border-b-gray-500 focus:outline-none font-helvetica-ultra-light'
    }))
    birthdate = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'text-iwhite w-full px-4 py-2 bg-iblack  border-b-2 border-b-gray-500 focus:outline-none font-helvetica-ultra-light'
    }))
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'file-input'
    }))

    class Meta:
        model = Profile
        fields = ['profile_picture', 'birthdate', 'first_name', 'last_name', 'email', 'phone_number', 'password']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email
            self.fields['phone_number'].initial = user.phone_number
            self.fields['birthdate'].initial = user.profile.birthdate
            self.fields['password'].widget = forms.HiddenInput()  # Keep as hidden if not being changed directly

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        user.save()

        if commit:
            profile.save()
        return profile