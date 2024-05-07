from django.db import models 
from django.db.models import F
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

GENRE_CHOICES = [
    ('fiction', _('Fiction')),
    ('non-fiction', _('Non-Fiction')),
    ('mystery', _('Mystery')),
    ('fantasy', _('Fantasy')),
    ('biography', _('Biography')),
    ('history', _('History')),
    ('science', _('Science')),
    ('romance', _('Romance')),
    ('horror', _('Horror')),
    ('adventure', _('Adventure')),
   
]

LANGUAGE_CHOICES = [
    ('EN', _('English')),
    ('FR', _('French')),
    ('AR', _('Arabic')),
    ('ES', _('Spanish')),
    ('DE', _('German')),
    ('IT', _('Italian')),
    ('RU', _('Russian')),
    ('JA', _('Japanese')),
    
]

class Book(models.Model):
    photo = models.ImageField(upload_to='book_photos/')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField()
    date_edition = models.DateField()
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    
    genre = models.CharField(max_length=255, choices=GENRE_CHOICES)
    
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES)

    class Meta:
        ordering = ['title']

    def is_available(self):
        """Check if the book is available."""
        return self.quantity > 0

    @classmethod
    def find_book(cls, title):
        """Find a book by its title."""
        return cls.objects.filter(title__icontains=title)

    def return_book(self):
        """Return a book."""
        self.quantity += 1
        self.save()
        return self

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)  # Optional phone number

    # Define unique related_names for groups and user_permissions to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True,
        verbose_name=_('groups'),
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True,
        verbose_name=_('user permissions'),
        help_text=_('Specific permissions for this user.'),
    )
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_phone_number(self):
        return self.user.phone_number if self.user else None

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class BorrowHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='borrowed_books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_history')
    date_borrowed = models.DateTimeField(default=timezone.now)
    date_returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"

    def mark_as_returned(self):
        """Mark the book as returned."""
        self.date_returned = timezone.now()
        self.save()

        # Optionally, update the book's quantity if managing stock
        self.book.return_book()

    class Meta:
        ordering = ['-date_borrowed']
    

class ReturnedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_returned = models.DateField()
    validated = models.BooleanField(default=False)