from django.db import models

class Book(models.Model):
    # A character field for the book's title.
    # The max_length attribute is required for CharField.
    title = models.CharField(max_length=255)

    # A character field for the book's author.
    author = models.CharField(max_length=255)

    # A positive integer field for the publication year.
    publication_year = models.PositiveIntegerField()

    # A text field for a brief summary of the book.
    summary = models.TextField(blank=True, null=True)

    # A boolean field to track if the book is available.
    is_available = models.BooleanField(default=True)

    def __str__(self):
        """
        Returns a string representation of the Book model.
        This is what will be displayed in the Django admin site.
        """
        return f"{self.title} by {self.author}"
