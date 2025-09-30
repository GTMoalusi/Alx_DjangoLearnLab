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

# from rest_framework import generics

# # Import the models
# from .models import ProjectItem, Author, Book
# # Import the serializers (These must now be found after updating serializers.py)
# from .serializers import (
#     ProjectItemSerializer,
#     AuthorSerializer,
#     BookSerializer
# )

# # Views for ProjectItem (Basic CRUD operations)
# class ProjectItemListCreate(generics.ListCreateAPIView):
#     """View to list all ProjectItems or create a new one."""
#     queryset = ProjectItem.objects.all()
#     serializer_class = ProjectItemSerializer

# class ProjectItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     """View to retrieve, update, or delete a single ProjectItem."""
#     queryset = ProjectItem.objects.all()
#     serializer_class = ProjectItemSerializer

# # Views for Author
# class AuthorListCreate(generics.ListCreateAPIView):
#     """View to list all Authors or create a new one."""
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class AuthorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     """View to retrieve, update, or delete a single Author."""
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# # Views for Book
# class BookListCreate(generics.ListCreateAPIView):
#     """View to list all Books or create a new one."""
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     """View to retrieve, update, or delete a single Book."""
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

# --- View 1: List all Books and Create a new Book ---

class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    Handles GET and POST requests to the /books/ endpoint.

    GET (List all): Allowed for all users (read-only access).
    POST (Create new book): Restricted to authenticated users only (write access).
    """
    
    # Required attributes for Generic Views:
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Permission Setup (Step 4):
    # Allows read (GET) for anyone, but requires authentication for write (POST, PUT, DELETE, PATCH).
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Customization Example (Step 3 - Optional hook):
    # def perform_create(self, serializer):
    #     """Customizes the creation behavior, e.g., setting the creating user."""
    #     # Example: If your Book model had a 'created_by' field, you could set it here.
    #     serializer.save()


# --- View 2: Retrieve, Update, and Delete a specific Book ---

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET, PUT, PATCH, and DELETE requests to the /books/<int:pk>/ endpoint.

    GET (Retrieve detail): Allowed for all users (read-only access).
    PUT/PATCH/DELETE (Update/Destroy): Restricted to authenticated users only (write access).
    """
    
    # Required attributes for Generic Views:
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Permission Setup (Step 4):
    # Applies the same read/write permissions as the ListCreate view.
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Customization Example (Step 3 - Optional hook):
    # def perform_destroy(self, instance):
    #     """Customizes the destruction behavior, e.g., adding an audit log."""
    #     print(f"User {self.request.user} is deleting book: {instance.title}")
    #     instance.delete()
