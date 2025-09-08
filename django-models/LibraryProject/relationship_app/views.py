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
    # This line is updated with the full path to the template.
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    """
    Displays the details of a single Library object.
    It automatically fetches the object based on the primary key (pk) in the URL.
    """
    model = Library
    # The template_name has been updated to use the full path.
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
