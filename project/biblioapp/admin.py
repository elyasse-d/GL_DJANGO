from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.admin.models import LogEntry

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone_number']

admin.site.register(CustomUser, CustomUserAdmin)

class CustomLogEntry(LogEntry):
    class Meta:
        proxy = True

# Ne pas définir le champ user dans CustomLogEntry

admin.site.register(CustomLogEntry)
