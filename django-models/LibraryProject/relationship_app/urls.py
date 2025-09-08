from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    # Maps the URL "books/" to the list_books view
    path('books/', views.list_books, name='list_books'),
    
    # Maps a URL like "library/1/" to the LibraryDetailView
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
