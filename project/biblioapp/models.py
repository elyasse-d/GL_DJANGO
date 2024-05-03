from django.db import models
from django.contrib.auth.models import User

# model Book starts here  

class Book(models.Model):
    photo = models.ImageField(upload_to='book_photos/')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField()
    date_edition = models.DateField()
    quantity = models.IntegerField(default=0)
    genre = models.CharField(max_length=255)  # Ou vous pouvez utiliser un autre modèle pour les genres si vous préférez
    language = models.CharField(max_length=100)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def is_available(self):
        """Vérifie si le livre est disponible."""
        return self.quantity > 0

    @classmethod
    def find_book(cls, title):
        """Trouve un livre par son titre."""
        try:
            return cls.objects.get(title=title)
        except cls.DoesNotExist:
            return None

    def rent_book(self, user):
        """Emprunte un livre."""
        if self.is_available():
            self.quantity -= 1
            self.borrower = user
            self.save()
            return 1  # Succès
        else:
            return 0  # Échec, pas de stock disponible

    def return_book(self):
        """Retourne un livre."""
        self.quantity += 1
        self.borrower = None
        self.save()
        return self

    def __str__(self):
        return self.title

# end of book model 