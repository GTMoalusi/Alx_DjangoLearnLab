# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics
# from .models import ProjectItem
# from .serializers import ProjectItemSerializer

# class ProjectItemListCreate(generics.ListCreateAPIView):
#     """
#     View for listing all ProjectItems (GET request) 
#     and creating a new ProjectItem (POST request).
    
#     This view uses the ProjectItemSerializer to handle data formatting and validation.
#     """
#     # Define the queryset (all items we can list)
#     queryset = ProjectItem.objects.all()
    
#     # Define the serializer class to use
#     serializer_class = ProjectItemSerializer

# class ProjectItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     """
#     View for retrieving a single ProjectItem (GET request with ID),
#     updating it (PUT/PATCH requests), and deleting it (DELETE request).
#     """
#     # Define the queryset (all items we can look up)
#     queryset = ProjectItem.objects.all()
    
#     # Define the serializer class to use
#     serializer_class = ProjectItemSerializer

from rest_framework import generics

# Import the models
from .models import ProjectItem, Author, Book
# Import the serializers (These must now be found after updating serializers.py)
from .serializers import (
    ProjectItemSerializer,
    AuthorSerializer,
    BookSerializer
)

# Views for ProjectItem (Basic CRUD operations)
class ProjectItemListCreate(generics.ListCreateAPIView):
    """View to list all ProjectItems or create a new one."""
    queryset = ProjectItem.objects.all()
    serializer_class = ProjectItemSerializer

class ProjectItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """View to retrieve, update, or delete a single ProjectItem."""
    queryset = ProjectItem.objects.all()
    serializer_class = ProjectItemSerializer

# Views for Author
class AuthorListCreate(generics.ListCreateAPIView):
    """View to list all Authors or create a new one."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """View to retrieve, update, or delete a single Author."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Views for Book
class BookListCreate(generics.ListCreateAPIView):
    """View to list all Books or create a new one."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """View to retrieve, update, or delete a single Book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
