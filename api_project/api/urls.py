from django.urls import path
from .views import BookList, BookDetail

# Defines the URL patterns for the 'api' app
urlpatterns = [
    # Route for listing all books and creating a new one
    path('books/', BookList.as_view(), name='book-list'),
    
    # Route for retrieving, updating, or deleting a single book by its primary key
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]
