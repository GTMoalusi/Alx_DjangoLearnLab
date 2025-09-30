# api/urls.py
# from django.urls import path
# from .views import ProjectItemListCreate, ProjectItemRetrieveUpdateDestroy

# # Define the app name for namespace resolution (useful later)
# app_name = 'api'

# # List of URL patterns
# urlpatterns = [
#     # Route for listing all items and creating a new one (GET / POST)
#     # URL: /api/items/
#     path('items/', ProjectItemListCreate.as_view(), name='item-list-create'),
    
#     # Route for retrieving, updating, or deleting a specific item (GET / PUT / DELETE)
#     # The <int:pk> captures the primary key (ID) from the URL.
#     # URL: /api/items/1/ (e.g.)
#     path('items/<int:pk>/', ProjectItemRetrieveUpdateDestroy.as_view(), name='item-detail'),
# ]

# from django.urls import path
# from .views import (
#     BookListCreateAPIView, 
#     BookRetrieveUpdateDestroyAPIView
# )

# # Define the URL patterns for the API
# urlpatterns = [
#     # 1. Endpoint for listing all books and creating a new book
#     # URL: /api/books/
#     path('books/', 
#          BookListCreateAPIView.as_view(), 
#          name='book-list-create'),

#     # 2. Endpoint for retrieving, updating, or deleting a single book
#     # URL: /api/books/<pk>/ (e.g., /api/books/1/)
#     path('books/<int:pk>/', 
#          BookRetrieveUpdateDestroyAPIView.as_view(), 
#          name='book-detail'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     # Paths for listing all books (GET) and creating a new book (POST)
#     # Both List and Create use the same path but are separated by HTTP method in views.py
#     path('books/', views.ListView.as_view(), name='book-list'),
#     path('books/', views.CreateView.as_view(), name='book-create'),

#     # Paths for detailed operations on a single book, requiring the primary key (pk)
#     # Detail (GET), Update (PUT/PATCH), and Delete (DELETE)
#     path('books/<int:pk>/', views.DetailView.as_view(), name='book-detail'),
#     path('books/<int:pk>/', views.UpdateView.as_view(), name='book-update'),
#     path('books/<int:pk>/', views.DeleteView.as_view(), name='book-delete'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     # 1. List (GET) & Create (POST) endpoints
#     # Use 'books/' for the list view (GET)
#     path('books/', views.ListView.as_view(), name='book-list'),
    
#     # Explicitly name a path for 'create' operation (POST to /api/books/create)
#     # This addresses the check requirement for "books/create"
#     path('books/create/', views.CreateView.as_view(), name='book-create'),

#     # 2. Detail (GET), Update (PUT/PATCH), and Delete (DELETE) endpoints
#     # Use 'books/<int:pk>/' for the detail view (GET)
#     path('books/<int:pk>/', views.DetailView.as_view(), name='book-detail'),
    
#     # Explicitly name a path for 'update' operation
#     # This addresses the check requirement for "books/update"
#     path('books/<int:pk>/update/', views.UpdateView.as_view(), name='book-update'),
    
#     # Explicitly name a path for 'delete' operation
#     # This addresses the check requirement for "books/delete"
#     path('books/<int:pk>/delete/', views.DeleteView.as_view(), name='book-delete'),
# ]

from django.urls import path
from . import views # Assuming you update views.py to have combined views

urlpatterns = [
    # 1. List (GET) & Create (POST) endpoint
    # This single path now uses the name 'book-list-create'
    # which your test file is looking for. It should point to a single 
    # view (e.g., BookListCreateAPIView in views.py) that handles both GET and POST.
    path('books/', views.BookListCreateView.as_view(), name='book-list-create'),
    
    # 2. Detail (GET), Update (PUT/PATCH), and Delete (DELETE) endpoint
    # This single path handles all detail operations using the <int:pk> parameter.
    # It should point to a single view (e.g., BookRetrieveUpdateDestroyAPIView in views.py).
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    
    # NOTE: The explicit separate paths for /create/, /update/, and /delete/
    # have been removed, as this updated structure is standard REST practice
    # (e.g., use PUT/PATCH on /books/1/ for update, DELETE on /books/1/ for delete).
]
