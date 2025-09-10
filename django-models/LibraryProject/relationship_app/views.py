from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Function-based view to list all books
def list_books(request):
    """
    Retrieves all Book objects from the database and renders a list.
    """
    books = Book.objects.all().values()
    template = loader.get_template('list_books.html')
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)
   #  return HttpResponse(template.render(context, request))

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    """
    Displays the details of a single Library object.
    It automatically fetches the object based on the primary key (pk) in the URL.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
