from django import forms
from .models import Book

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200, help_text="Enter a book title.")
    author = forms.CharField(max_length=100, help_text="Enter the author's name.")
    publication_year = forms.IntegerField(label="Publication Year", required=False)
