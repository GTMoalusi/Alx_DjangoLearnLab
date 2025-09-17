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

# from django import forms
# from .models import Book, Library

# class BookForm(forms.ModelForm):
#     """
#     A form for creating and updating Book instances.
#     This form uses the 'isbn' field from the Book model.
#     """
#     class Meta:
#         model = Book
#         fields = ['title', 'author', 'isbn', 'library']

# class LibraryForm(forms.ModelForm):
#     """
#     A form for creating and updating Library instances.
#     """
#     class Meta:
#         model = Library
#         fields = ['name', 'location']

# from django import forms
# from .models import Book, Library

# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         # Make sure the fields list includes 'isbn' and 'library'
#         fields = ['title', 'author', 'publication_year', 'isbn', 'library']

# from django import forms
# from .models import Book, Library

# class BookForm(forms.ModelForm):
#     """
#     Form for creating and updating Book objects.
#     """
#     class Meta:
#         model = Book
#         # The fields listed here MUST match the fields in your Book model.
#         fields = ['title', 'author', 'publication_year', 'isbn', 'library']

# class LibraryForm(forms.ModelForm):
#     """
#     Form for creating and updating Library objects.
#     """
#     class Meta:
#         model = Library
#         fields = '__all__'

from django import forms
from .models import Book, Library

class BookForm(forms.ModelForm):
    """
    Form for creating and updating Book objects.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'isbn', 'library']

class LibraryForm(forms.ModelForm):
    """
    Form for creating and updating Library objects.
    """
    class Meta:
        model = Library
        fields = ['name', 'location']
