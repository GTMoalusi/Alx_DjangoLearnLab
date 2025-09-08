from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    """
    Retrieves all Book objects from the database and renders a list.
    """
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'list_books.html', context)

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    """
    Displays the details of a single Library object.
    It automatically fetches the object based on the primary key (pk) in the URL.
    """
    model = Library
    template_name = 'library_detail.html', 'list_books.html'
    context_object_name = 'library'