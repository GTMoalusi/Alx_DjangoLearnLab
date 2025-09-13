# from django.http import HttpResponse
# from django.template import loader
# from django.shortcuts import render
# from django.views.generic import DetailView
# from .models import Book
# from .models import Library
# from django.views.generic.detail import DetailView

# # Function-based view to list all books
# def list_books(request):
#     """
#     Retrieves all Book objects from the database and renders a list.
#     """
#     books = Book.objects.all().values()
#     template = loader.get_template('list_books.html')
#     context = {
#         'books': books
#     }
#     return render(request, 'relationship_app/list_books.html', context)
#    #  return HttpResponse(template.render(context, request))

# # Class-based view to display details for a specific library
# class LibraryDetailView(DetailView):
#     """
#     Displays the details of a single Library object.
#     It automatically fetches the object based on the primary key (pk) in the URL.
#     """
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'

# from django.shortcuts import render
# from django.views.generic import DetailView
# from .models import Book, Library

# # Function-based view to list all books
# def list_books(request):
#     """
#     Retrieves all Book objects from the database and renders a list.
#     """
#     books = Book.objects.all()
#     context = {
#         'books': books
#     }
#     return render(request, 'relationship_app/list_books.html', context)

# # Class-based view to display details for a specific library
# class LibraryDetailView(DetailView):
#     """
#     Displays the details of a single Library object.
#     It automatically fetches the object based on the primary key (pk) in the URL.
#     """
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'

# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login, logout, authenticate
# from django.views.generic import DetailView
# from .models import Book, Library

# # Function-based view to list all books
# def list_books(request):
#     """
#     Retrieves all Book objects from the database and renders a list.
#     """
#     books = Book.objects.all()
#     context = {
#         'books': books
#     }
#     return render(request, 'relationship_app/list_books.html', context)

# # Class-based view to display details for a specific library
# class LibraryDetailView(DetailView):
#     """
#     Displays the details of a single Library object.
#     It automatically fetches the object based on the primary key (pk) in the URL.
#     """
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'

# # Function-based view for user registration
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('list_books')
#     else:
#         form = UserCreationForm()
#     return render(request, 'relationship_app/register.html', {'form': form})

# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login, logout
# from django.views.generic import DetailView
# from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.models import User
# from .models import Book, Library, UserProfile

# # Function-based view to list all books
# def list_books(request):
#     books = Book.objects.all()
#     context = {'books': books}
#     return render(request, 'relationship_app/list_books.html', context)

# # Class-based view to display details for a specific library
# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'

# # Function-based view for user registration
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('books')
#     else:
#         form = UserCreationForm()
#     return render(request, 'relationship_app/register.html', {'form': form})

# # Helper functions to check user roles
# def is_admin(user):
#     return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# def is_librarian(user):
#     return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# def is_member(user):
#     return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# # Role-based views
# @user_passes_test(is_admin, login_url='/login/')
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# @user_passes_test(is_librarian, login_url='/login/')
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# @user_passes_test(is_member, login_url='/login/')
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')

# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required, permission_required
# from .models import Book, Library
# from .forms import BookForm, LibraryForm

# def index(request):
#     """
#     Main view to display all books and libraries.
#     """
#     books = Book.objects.all()
#     libraries = Library.objects.all()
#     context = {'books': books, 'libraries': libraries}
#     return render(request, 'relationship_app/index.html', context)

# # --- Book Views with Permissions ---

# @login_required
# @permission_required('relationship_app.can_add_book', raise_exception=True)
# def add_book(request):
#     """
#     View to handle adding a new book.
#     Requires 'can_add_book' permission.
#     """
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = BookForm()
#     return render(request, 'relationship_app/add_book.html', {'form': form})

# @login_required
# @permission_required('relationship_app.can_change_book', raise_exception=True)
# def edit_book(request, pk):
#     """
#     View to handle editing an existing book.
#     Requires 'can_change_book' permission.
#     """
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = BookForm(instance=book)
#     return render(request, 'relationship_app/edit_book.html', {'form': form})

# @login_required
# @permission_required('relationship_app.can_delete_book', raise_exception=True)
# def delete_book(request, pk):
#     """
#     View to handle deleting a book.
#     Requires 'can_delete_book' permission.
#     """
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         book.delete()
#         return redirect('index')
#     return render(request, 'relationship_app/delete_book_confirm.html', {'book': book})

# # --- Library Views (Unchanged) ---

# def add_library(request):
#     if request.method == 'POST':
#         form = LibraryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = LibraryForm()
#     return render(request, 'relationship_app/add_library.html', {'form': form})

# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required, permission_required
# from .models import Book, Library
# from .forms import BookForm, LibraryForm

# def index(request):
#     """
#     Main view to display all books and libraries.
#     """
#     books = Book.objects.all()
#     libraries = Library.objects.all()
#     context = {'books': books, 'libraries': libraries}
#     return render(request, 'relationship_app/index.html', context)

# # --- Book Views with Permissions ---

# @login_required
# @permission_required('relationship_app.can_add_book', raise_exception=True)
# def add_book(request):
#     """
#     View to handle adding a new book.
#     Requires 'can_add_book' permission.
#     """
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = BookForm()
#     return render(request, 'relationship_app/add_book.html', {'form': form})

# @login_required
# @permission_required('relationship_app.can_change_book', raise_exception=True)
# def edit_book(request, pk):
#     """
#     View to handle editing an existing book.
#     Requires 'can_change_book' permission.
#     """
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = BookForm(instance=book)
#     return render(request, 'relationship_app/edit_book.html', {'form': form})

# @login_required
# @permission_required('relationship_app.can_delete_book', raise_exception=True)
# def delete_book(request, pk):
#     """
#     View to handle deleting a book.
#     Requires 'can_delete_book' permission.
#     """
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         book.delete()
#         return redirect('index')
#     return render(request, 'relationship_app/delete_book_confirm.html', {'book': book})

# # --- Library Views ---

# @login_required
# @permission_required('relationship_app.can_add_library', raise_exception=True)
# def add_library(request):
#     """
#     View to handle adding a new library.
#     Requires 'can_add_library' permission.
#     """
#     if request.method == 'POST':
#         form = LibraryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = LibraryForm()
#     return render(request, 'relationship_app/add_library.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book, Library
from .forms import BookForm, LibraryForm

def index(request):
    """
    Main view to display all books and libraries.
    """
    books = Book.objects.all()
    libraries = Library.objects.all()
    context = {'books': books, 'libraries': libraries}
    return render(request, 'relationship_app/index.html', context)

# --- Book Views with Permissions ---

@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    """
    View to handle adding a new book.
    Requires 'can_add_book' permission.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    """
    View to handle editing an existing book.
    Requires 'can_change_book' permission.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    """
    View to handle deleting a book.
    Requires 'can_delete_book' permission.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('index')
    return render(request, 'relationship_app/delete_book_confirm.html', {'book': book})

# --- Library Views ---

@login_required
@permission_required('relationship_app.can_add_library', raise_exception=True)
def add_library(request):
    """
    View to handle adding a new library.
    Requires 'can_add_library' permission.
    """
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LibraryForm()
    return render(request, 'relationship_app/add_library.html', {'form': form})
