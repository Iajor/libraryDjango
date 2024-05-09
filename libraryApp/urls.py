from django.urls import path
from libraryApp.views import *

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('custom-books/', CustomBookListView.as_view(), name='custom-book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
