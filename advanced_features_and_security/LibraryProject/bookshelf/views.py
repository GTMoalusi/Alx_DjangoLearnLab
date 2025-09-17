from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# This is a view that lists all books. It does not require any special permissions.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})


# This view requires the 'bookshelf.can_create' permission to be accessed.
# The raise_exception=True argument ensures a 403 Forbidden error is raised
# if the user does not have the permission.
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Logic to handle book creation
        # book_form = BookForm(request.POST)
        # if book_form.is_valid():
        #     book_form.save()
        return redirect('book_list')
    return render(request, 'bookshelf/create_book.html')


# This view requires the 'bookshelf.can_edit' permission.
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        # Logic to handle book editing
        # book_form = BookForm(request.POST, instance=book)
        # if book_form.is_valid():
        #     book_form.save()
        return redirect('book_list')
    return render(request, 'bookshelf/edit_book.html', {'book': book})


# This view requires the 'bookshelf.can_delete' permission.
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/confirm_delete.html', {'book': book})
