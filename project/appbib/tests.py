from django.test import TestCase
from django.utils import timezone
from .models import Book


# cette partie pour tester le model Book

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Book.objects.create(
            photo='book_photos/test_photo.jpg',
            title='Test Book',
            author='Test Author',
            summary='This is a test summary.',
            date_edition=timezone.now().date(),
            quantity=5,
            genre='Test Genre',
            language='English'
        )

    def test_photo_field(self):
        book = Book.objects.get(id=1)
        field = book._meta.get_field('photo')
        self.assertTrue(field.upload_to == 'book_photos/')

    def test_title_field(self):
        book = Book.objects.get(id=1)
        title = book.title
        self.assertEqual(title, 'Test Book')

    def test_author_field(self):
        book = Book.objects.get(id=1)
        author = book.author
        self.assertEqual(author, 'Test Author')

    def test_summary_field(self):
        book = Book.objects.get(id=1)
        summary = book.summary
        self.assertEqual(summary, 'This is a test summary.')

    def test_date_edition_field(self):
        book = Book.objects.get(id=1)
        date_edition = book.date_edition
        self.assertEqual(date_edition, timezone.now().date())

    def test_quantity_field(self):
        book = Book.objects.get(id=1)
        quantity = book.quantity
        self.assertEqual(quantity, 5)

    def test_genre_field(self):
        book = Book.objects.get(id=1)
        genre = book.genre
        self.assertEqual(genre, 'Test Genre')

    def test_language_field(self):
        book = Book.objects.get(id=1)
        language = book.language
        self.assertEqual(language, 'English')

    def test_borrower_field(self):
        book = Book.objects.get(id=1)
        borrower = book.borrower
        self.assertIsNone(borrower)

# fin de test model Book