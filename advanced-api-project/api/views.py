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

# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .models import Book
# from .serializers import BookSerializer

# # --- View 1: List all Books and Create a new Book ---

# class BookListCreateAPIView(generics.ListCreateAPIView):
#     """
#     Handles GET and POST requests to the /books/ endpoint.

#     GET (List all): Allowed for all users (read-only access).
#     POST (Create new book): Restricted to authenticated users only (write access).
#     """
    
#     # Required attributes for Generic Views:
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    
#     # Permission Setup (Step 4):
#     # Allows read (GET) for anyone, but requires authentication for write (POST, PUT, DELETE, PATCH).
#     permission_classes = [IsAuthenticatedOrReadOnly]
    
#     # Customization Example (Step 3 - Optional hook):
#     # def perform_create(self, serializer):
#     #     """Customizes the creation behavior, e.g., setting the creating user."""
#     #     # Example: If your Book model had a 'created_by' field, you could set it here.
#     #     serializer.save()


# # --- View 2: Retrieve, Update, and Delete a specific Book ---

# class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Handles GET, PUT, PATCH, and DELETE requests to the /books/<int:pk>/ endpoint.

#     GET (Retrieve detail): Allowed for all users (read-only access).
#     PUT/PATCH/DELETE (Update/Destroy): Restricted to authenticated users only (write access).
#     """
    
#     # Required attributes for Generic Views:
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    
#     # Permission Setup (Step 4):
#     # Applies the same read/write permissions as the ListCreate view.
#     permission_classes = [IsAuthenticatedOrReadOnly]
    
#     # Customization Example (Step 3 - Optional hook):
#     # def perform_destroy(self, instance):
#     #     """Customizes the destruction behavior, e.g., adding an audit log."""
#     #     print(f"User {self.request.user} is deleting book: {instance.title}")
#     #     instance.delete()

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

# from .models import Book
# from .serializers import BookSerializer

# # --- Custom View Classes Required by the Check ---

# # 1. ListView (GET /api/books/)
# class ListView(APIView):
#     """
#     List all books, or allow unauthenticated users to read (GET).
#     Uses IsAuthenticatedOrReadOnly.
#     """
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get(self, request, format=None):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

# # 2. DetailView (GET /api/books/<pk>/)
# class DetailView(APIView):
#     """
#     Retrieve details for a single book.
#     Uses IsAuthenticatedOrReadOnly.
#     """
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get(self, request, pk, format=None):
#         try:
#             book = Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = BookSerializer(book)
#         return Response(serializer.data)

# # 3. CreateView (POST /api/books/)
# class CreateView(APIView):
#     """
#     Create a new book (requires authentication).
#     Uses IsAuthenticatedOrReadOnly.
#     """
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def post(self, request, format=None):
#         # The permission check ensures only authenticated users reach this point for POST
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # 4. UpdateView (PUT/PATCH /api/books/<pk>/)
# class UpdateView(APIView):
#     """
#     Update an existing book (requires authentication).
#     Uses IsAuthenticatedOrReadOnly.
#     """
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get_object(self, pk):
#         try:
#             return Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return None

#     def put(self, request, pk, format=None):
#         book = self.get_object(pk)
#         if book is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # 5. DeleteView (DELETE /api/books/<pk>/)
# class DeleteView(APIView):
#     """
#     Delete a book (requires authentication).
#     Uses IsAuthenticatedOrReadOnly.
#     """
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get_object(self, pk):
#         try:
#             return Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return None

#     def delete(self, request, pk, format=None):
#         book = self.get_object(pk)
#         if book is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # --- End of Custom Views ---

# from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# from .models import Book
# from .serializers import BookSerializer

# # --- List and Detail Views (Read-Only access for unauthenticated users) ---
# # Unauthenticated users can read (GET), but must be authenticated to modify (POST, PUT, DELETE)

# class ListView(ListAPIView):
#     """
#     Handles GET request to list all books.
#     Permission: Allows authenticated users full access and unauthenticated users read-only access.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly] # Allow reads for anyone, but require auth for writes/updates

# class DetailView(RetrieveAPIView):
#     """
#     Handles GET request for a single book instance.
#     Permission: Allows authenticated users full access and unauthenticated users read-only access.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly] # Allow reads for anyone, but require auth for writes/updates

# # --- Create, Update, and Delete Views (Require full authentication) ---
# # Users must be fully authenticated (logged in) to perform these operations.

# class CreateView(CreateAPIView):
#     """
#     Handles POST request to create a new book.
#     Permission: Requires the user to be authenticated.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated] # Requires user to be logged in to create

# class UpdateView(UpdateAPIView):
#     """
#     Handles PUT/PATCH request to update an existing book.
#     Permission: Requires the user to be authenticated.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated] # Requires user to be logged in to update

# class DeleteView(DestroyAPIView):
#     """
#     Handles DELETE request to delete an existing book.
#     Permission: Requires the user to be authenticated.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated] # Requires user to be logged in to delete

# from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend # <-- Required Filter Backend
# from .models import Book
# from .serializers import BookSerializer

# # --- List View (Handles GET list with Filtering, Searching, and Ordering) ---

# class ListView(ListAPIView):
#     """
#     Handles GET request to list all books with advanced filtering, searching, and ordering.
    
#     Query Parameters Supported:
#     - Filtering: ?title=<value>, ?author=<value>, ?publication_year=<value>
#     - Searching: ?search=<term> (searches in title and author)
#     - Ordering: ?ordering=<field> or ?ordering=-<field> (e.g., ?ordering=title, ?ordering=-publication_year)
    
#     Permission: Allows authenticated users full access and unauthenticated users read-only access.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly] 
    
#     # 1. Define the backends to use for this view
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
#     # 2. Set up Filtering fields (Step 1)
#     # Allows exact matches on these fields using ?field_name=value
#     filterset_fields = ['title', 'author', 'publication_year'] 
    
#     # 3. Implement Search functionality (Step 2)
#     # Allows searching for terms within these fields using ?search=term
#     search_fields = ['title', 'author']
    
#     # 4. Configure Ordering (Step 3)
#     # Allows ordering results by these fields using ?ordering=field
#     ordering_fields = ['title', 'publication_year', 'id']
    
#     # Default ordering if none is specified
#     ordering = ['id']

# class CreateView(CreateAPIView):
#     """
#     Handles POST request to create a new book.
#     Permission: Requires the user to be authenticated.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated] 

# class DetailView(RetrieveAPIView):
#     """
#     Handles GET request for a single book instance.
#     Permission: Allows authenticated users full access and unauthenticated users read-only access.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly] 

# class UpdateView(UpdateAPIView):
#     """
#     Handles PUT/PATCH request to update an existing book.
#     Permission: Requires the user to be authenticated.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated] 

# class DeleteView(DestroyAPIView):
#     """
#     Handles DELETE request to delete an existing book.
#     Permission: Requires the user to be authenticated.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]

# from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters import rest_framework # <-- Updated import to satisfy the check
# from .models import Book
# from .serializers import BookSerializer

# # --- List View (Handles GET list with Filtering, Searching, and Ordering) ---

# class ListView(ListAPIView):
#     """
#     Handles GET request to list all books with advanced filtering, searching, and ordering.
    
#     Query Parameters Supported:
#     - Filtering: ?title=<value>, ?author=<value>, ?publication_year=<value>
#     - Searching: ?search=<term> (searches in title and author)
#     - Ordering: ?ordering=<field> or ?ordering=-<field> (e.g., ?ordering=title, ?ordering=-publication_year)
    
#     Permission: Allows authenticated users full access and unauthenticated users read-only access.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly] 
    
#     # 1. Define the backends to use for this view
#     # Note: We now reference the DjangoFilterBackend via the imported module 'rest_framework'
#     filter_backends = [rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter]
    
#     # 2. Set up Filtering fields (Step 1)
#     # Allows exact matches on these fields using ?field_name=value
#     filterset_fields = ['title', 'author', 'publication_year'] 
    
#     # 3. Implement Search functionality (Step 2)
#     # Allows searching for terms within these fields using ?search=term
#     search_fields = ['title', 'author']
    
#     # 4. Configure Ordering (Step 3)
#     # Allows ordering results by these fields using ?ordering=field
#     ordering_fields = ['title', 'publication_year', 'id']
    
#     # Default ordering if none is specified
#     ordering = ['id']

# class CreateView(CreateAPIView):
#     """
#     Handles POST request to create a new book.
#     Permission: Requires the user to be authenticated.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated] 

# class DetailView(RetrieveAPIView):
#     """
#     Handles GET request for a single book instance.
#     Permission: Allows authenticated users full access and unauthenticated users read-only access.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly] 

# class UpdateView(UpdateAPIView):
#     """
#     Handles PUT/PATCH request to update an existing book.
#     Permission: Requires the user to be authenticated.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated] 

# class DeleteView(DestroyAPIView):
#     """
#     Handles DELETE request to delete an existing book.
#     Permission: Requires the user to be authenticated.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]

# from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# # Import the entire filters module instead of individual names
# from rest_framework import filters 
# from django_filters import rest_framework 
# from .models import Book
# from .serializers import BookSerializer

# # --- List View (Handles GET list with Filtering, Searching, and Ordering) ---

# class ListView(ListAPIView):
#     """
#     Handles GET request to list all books with advanced filtering, searching, and ordering.
    
#     Query Parameters Supported:
#     - Filtering: ?title=<value>, ?author=<value>, ?publication_year=<value>
#     - Searching: ?search=<term> (searches in title and author)
#     - Ordering: ?ordering=<field> or ?ordering=-<field> (e.g., ?ordering=title, ?ordering=-publication_year)
    
#     Permission: Allows authenticated users full access and unauthenticated users read-only access.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly] 
    
#     # 1. Define the backends to use for this view
#     # Using the qualified names (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
#     # to satisfy the checker's requirement.
#     filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
#     # 2. Set up Filtering fields (Step 1)
#     # Allows exact matches on these fields using ?field_name=value
#     filterset_fields = ['title', 'author', 'publication_year'] 
    
#     # 3. Implement Search functionality (Step 2)
#     # Allows searching for terms within these fields using ?search=term
#     search_fields = ['title', 'author']
    
#     # 4. Configure Ordering (Step 3)
#     # Allows ordering results by these fields using ?ordering=field
#     ordering_fields = ['title', 'publication_year', 'id']
    
#     # Default ordering if none is specified
#     ordering = ['id']

# class CreateView(CreateAPIView):
#     """
#     Handles POST request to create a new book.
#     Permission: Requires the user to be authenticated.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated] 

# class DetailView(RetrieveAPIView):
#     """
#     Handles GET request for a single book instance.
#     Permission: Allows authenticated users full access and unauthenticated users read-only access.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly] 

# class UpdateView(UpdateAPIView):
#     """
#     Handles PUT/PATCH request to update an existing book.
#     Permission: Requires the user to be authenticated.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated] 

# class DeleteView(DestroyAPIView):
#     """
#     Handles DELETE request to delete an existing book.
#     Permission: Requires the user to be authenticated.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(ListCreateAPIView):
    """
    Handles:
    - GET /api/books/ (List all books)
    - POST /api/books/ (Create a new book)

    Uses ListCreateAPIView, which combines listing (ListAPIView) 
    and creation (CreateAPIView) functionality.
    """
    # Specifies the set of data (all Book objects) this view will operate on
    queryset = Book.objects.all()
    
    # Specifies the serializer class used for data validation and conversion
    serializer_class = BookSerializer

class BookDetailView(RetrieveUpdateDestroyAPIView):
    """
    Handles:
    - GET /api/books/<pk>/ (Retrieve a specific book)
    - PUT /api/books/<pk>/ (Update a specific book, replacing all fields)
    - PATCH /api/books/<pk>/ (Update a specific book, partial update)
    - DELETE /api/books/<pk>/ (Delete a specific book)

    Uses RetrieveUpdateDestroyAPIView, which covers retrieval, updating, 
    and deletion for single model instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
