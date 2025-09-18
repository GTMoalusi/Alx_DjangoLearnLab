# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import permission_required
# from .models import Book

# # This is a view that lists all books. It does not require any special permissions.
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'bookshelf/list_books.html', {'books': books})


# # This view requires the 'bookshelf.can_create' permission to be accessed.
# # The raise_exception=True argument ensures a 403 Forbidden error is raised
# # if the user does not have the permission.
# @permission_required('bookshelf.can_create', raise_exception=True)
# def create_book(request):
#     if request.method == 'POST':
#         # Logic to handle book creation
#         # book_form = BookForm(request.POST)
#         # if book_form.is_valid():
#         #     book_form.save()
#         return redirect('book_list')
#     return render(request, 'bookshelf/create_book.html')


# # This view requires the 'bookshelf.can_edit' permission.
# @permission_required('bookshelf.can_edit', raise_exception=True)
# def edit_book(request, book_id):
#     book = Book.objects.get(id=book_id)
#     if request.method == 'POST':
#         # Logic to handle book editing
#         # book_form = BookForm(request.POST, instance=book)
#         # if book_form.is_valid():
#         #     book_form.save()
#         return redirect('book_list')
#     return render(request, 'bookshelf/edit_book.html', {'book': book})


# # This view requires the 'bookshelf.can_delete' permission.
# @permission_required('bookshelf.can_delete', raise_exception=True)
# def delete_book(request, book_id):
#     book = Book.objects.get(id=book_id)
#     if request.method == 'POST':
#         book.delete()
#         return redirect('book_list')
#     return render(request, 'bookshelf/confirm_delete.html', {'book': book})

from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_GET, require_POST
from .models import Book
from .forms import ExampleForm # Import the new form

@require_GET
def book_list(request):
    """
    Renders a list of books, with an optional search feature.
    Safely handles user input to prevent SQL injection.
    """
    query = request.GET.get('q', '')

    if query:
        # Use Django's ORM to perform a safe, parameterized search.
        # The `Q` object allows for complex lookups (OR conditions in this case).
        # This prevents any possibility of SQL injection.
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    else:
        books = Book.objects.all()

    context = {'books': books}
    return render(request, 'bookshelf/book_list.html', context)

def csrf_failure(request, reason=""):
    """
    Custom view to handle CSRF verification failures.
    Provides a more user-friendly error message than the default.
    """
    return HttpResponseBadRequest(
        '<h1>CSRF Validation Failed</h1>'
        '<p>There was an issue with your request. Please try again.</p>'
    )

def add_book(request):
    """
    Handles a form for adding a new book, demonstrating secure input handling.
    """
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # Here, we're just demonstrating valid input handling
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            publication_year = form.cleaned_data['publication_year']
            
            # This is where you would save the data to the database
            # For example: Book.objects.create(title=title, author=author, publication_year=publication_year)
            
            # For this example, we'll just redirect to the book list page
            return redirect('book_list')
    else:
        form = ExampleForm() # An unbound form

    return render(request, 'bookshelf/form_example.html', {'form': form})
