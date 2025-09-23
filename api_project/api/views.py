# from django.shortcuts import render
# from rest_framework import generics
# from .models import Book
# from .serializers import BookSerializer

# # This view will handle GET and POST requests for a list of books.
# # It uses the Book model and the BookSerializer to perform these operations.
# # class BookList(generics.ListCreateAPIView):
# class BookList(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# # This view will handle GET, PUT, and DELETE requests for a single book.
# # It uses the Book model and the BookSerializer to perform these operations.
# # The `lookup_field` defaults to 'pk' (primary key), which is why our URL pattern uses <int:pk>.
# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# from rest_framework import viewsets
# from .serializers import BookSerializer
# from .models import Book

# # This ViewSet provides a complete set of CRUD operations
# # for the Book model.
# # It automatically handles listing all books, creating a new book,
# # retrieving a single book, updating a book, and deleting a book.
# class BookViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows books to be viewed or edited.
#     """
#     queryset = Book.objects.all().order_by('id')
#     serializer_class = BookSerializer

from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer

# This view is for listing all books and creating new ones.
# It uses the generics.ListCreateAPIView to handle both GET (list) and POST (create) requests.
class BookList(generics.ListCreateAPIView):
    # Specify the queryset to be used. This will get all Book objects from the database.
    queryset = Book.objects.all()
    # Specify the serializer to be used for converting complex data to native Python datatypes.
    serializer_class = BookSerializer

# This viewset provides all CRUD operations (create, retrieve, update, delete) for the Book model.
# The DefaultRouter in urls.py will automatically create the URL patterns for these operations.
class BookViewSet(viewsets.ModelViewSet):
    # The queryset that this viewset will operate on.
    queryset = Book.objects.all()
    # The serializer to use for data serialization and deserialization.
    serializer_class = BookSerializer
