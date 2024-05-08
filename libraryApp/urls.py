from django.urls import path
from libraryApp.views import AuthorListView, BookListView, BookDetailView

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
