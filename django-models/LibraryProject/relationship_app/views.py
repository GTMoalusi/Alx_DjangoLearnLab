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

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from .models import Book, Library, UserProfile

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Function-based view for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Helper functions to check user roles
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
