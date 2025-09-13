# from django import forms
# from .models import Book, Library

# class BookForm(forms.ModelForm):
#     """
#     A form for creating and updating Book instances.
#     """
#     class Meta:
#         model = Book
#         fields = ['title', 'author', 'publication_date', 'library']

# class LibraryForm(forms.ModelForm):
#     """
#     A form for creating and updating Library instances.
#     """
#     class Meta:
#         model = Library
#         fields = ['name', 'location']

from django import forms
from .models import Book, Library

class BookForm(forms.ModelForm):
    """
    A form for creating and updating Book instances.
    This form uses the 'isbn' field from the Book model.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'library']

class LibraryForm(forms.ModelForm):
    """
    A form for creating and updating Library instances.
    """
    class Meta:
        model = Library
        fields = ['name', 'location']
