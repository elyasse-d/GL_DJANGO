from django.contrib import admin
from .models import Book , BorrowHistory , CustomUser ,Profile ,ReturnedBook

# Register your models here.

admin.site.register(Book) 
admin.site.register(BorrowHistory)
admin.site.register(CustomUser)
admin.site.register(Profile)

admin.site.register(ReturnedBook)