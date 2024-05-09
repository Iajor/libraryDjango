from rest_framework import generics
from libraryApp.models import Author, Book
from libraryApp.serializers import AuthorSerializer, BookSerializer
from django.http import JsonResponse
from django.views.generic import View

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CustomBookListView(View):
    def get(self, request):
        name = request.GET.get('name')
        publication_year = request.GET.get('publication_year')
        edition = request.GET.get('edition')
        author = request.GET.get('author')

        books = Book.objects.all()
        if name:
            books = books.filter(name__icontains=name)
        if publication_year:
            books = books.filter(publication_year=publication_year)
        if edition:
            books = books.filter(edition=edition)
        if author:
            books = books.filter(authors__name__icontains=author)

        books_data = [{'id': book.id, 'name': book.name, 'edition': book.edition, 'publication_year': book.publication_year} for book in books]

        return JsonResponse({'books': books_data})

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = [
        'name',
        'edition',
        'publication_year',
        'authors',
    ]
