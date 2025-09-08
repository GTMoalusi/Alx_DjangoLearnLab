from django.db import models

class Author(models.Model):
    """
    A simple model representing an author.
    This model has no relationships to others defined here, but
    is a target for a ForeignKey.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book.
    - ForeignKey: This field establishes a many-to-one relationship.
      A single author can write many books, but each book has only one author.
      The `on_delete=models.CASCADE` argument ensures that if an Author is deleted,
      all of their associated books are also deleted.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author.name}"

class Library(models.Model):
    """
    Represents a library.
    - ManyToManyField: This creates a many-to-many relationship.
      A library can contain many books, and a single book can be in many different libraries.
      Django handles the creation of the intermediary join table automatically.
    """
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    """
    Represents a librarian.
    - OneToOneField: This field establishes a one-to-one relationship.
      Each librarian is uniquely associated with one library, and each library
      is uniquely associated with one librarian.
      The `on_delete=models.CASCADE` argument means if the Library is deleted,
      its associated Librarian is also deleted.
    """
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name