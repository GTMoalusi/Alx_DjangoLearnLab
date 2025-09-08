from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

def list_books(request):
    """
    Retrieves all Book objects from the database and renders a list.
    """
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    """
    Displays the details of a single Library object.
    It automatically fetches the object based on the primary key (pk) in the URL.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
