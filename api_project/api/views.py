from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# This view will handle GET and POST requests for a list of books.
# It uses the Book model and the BookSerializer to perform these operations.
# class BookList(generics.ListCreateAPIView):
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# This view will handle GET, PUT, and DELETE requests for a single book.
# It uses the Book model and the BookSerializer to perform these operations.
# The `lookup_field` defaults to 'pk' (primary key), which is why our URL pattern uses <int:pk>.
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
