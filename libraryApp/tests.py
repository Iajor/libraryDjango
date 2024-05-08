from django.test import TestCase
from rest_framework.test import APIClient
from libraryApp.models import Author, Book

class LibraryAPITest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(name='Test Book', edition=1, publication_year=2022)
        self.book.authors.add(self.author)

    def test_author_list(self):
        client = APIClient()
        response = client.get('/authors/')
        self.assertEqual(response.status_code, 200)

    def test_book_list(self):
        client = APIClient()
        response = client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_book_detail(self):
        client = APIClient()
        response = client.get(f'/books/{self.book.pk}/')
        self.assertEqual(response.status_code, 200)
