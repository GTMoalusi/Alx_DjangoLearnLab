# from django.urls import path
# from .views import BookList, BookDetail

# # Defines the URL patterns for the 'api' app
# urlpatterns = [
#     # Route for listing all books and creating a new one
#     path('books/', BookList.as_view(), name='book-list'),
    
#     # Route for retrieving, updating, or deleting a single book by its primary key
#     path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
# ]

# from django.shortcuts import render
# from rest_framework import generics
# from .models import Book
# from .serializers import BookSerializer

# # This view will handle GET and POST requests for a list of books.
# # It allows listing all books and creating a new book entry.
# class BookList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# # This view will handle GET, PUT, and DELETE requests for a single book.
# # It allows retrieving, updating, or deleting a specific book by its ID.
# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    # This path handles requests to the 'api/' base URL.
    # It links to the BookList view, which can be used to
    # retrieve a list of all books or create a new book.
    path('books/', BookList.as_view(), name='book-list'),

    # This path handles requests for a single book.
    # The <int:pk> part is a variable that captures the book's primary key (ID).
    # It links to the BookDetail view, which can be used to
    # retrieve, update, or delete a specific book.
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]
