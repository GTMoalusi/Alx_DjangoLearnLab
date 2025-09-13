# from django.db import models

# class Author(models.Model):
#     """
#     A simple model representing an author.
#     This model has no relationships to others defined here, but
#     is a target for a ForeignKey.
#     """
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# class Book(models.Model):
#     """
#     Represents a book.
#     - ForeignKey: This field establishes a many-to-one relationship.
#       A single author can write many books, but each book has only one author.
#       The `on_delete=models.CASCADE` argument ensures that if an Author is deleted,
#       all of their associated books are also deleted.
#     """
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.title} by {self.author.name}"

# class Library(models.Model):
#     """
#     Represents a library.
#     - ManyToManyField: This creates a many-to-many relationship.
#       A library can contain many books, and a single book can be in many different libraries.
#       Django handles the creation of the intermediary join table automatically.
#     """
#     name = models.CharField(max_length=200)
#     books = models.ManyToManyField(Book)

#     def __str__(self):
#         return self.name

# class Librarian(models.Model):
#     """
#     Represents a librarian.
#     - OneToOneField: This field establishes a one-to-one relationship.
#       Each librarian is uniquely associated with one library, and each library
#       is uniquely associated with one librarian.
#       The `on_delete=models.CASCADE` argument means if the Library is deleted,
#       its associated Librarian is also deleted.
#     """
#     name = models.CharField(max_length=200)
#     library = models.OneToOneField(Library, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# # Define choices for the user's role
# ROLE_CHOICES = (
#     ('Admin', 'Admin'),
#     ('Librarian', 'Librarian'),
#     ('Member', 'Member'),
# )

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)
#     publication_date = models.DateField()
#     library = models.ForeignKey('Library', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

# class Library(models.Model):
#     name = models.CharField(max_length=200)
#     address = models.CharField(max_length=250)

#     def __str__(self):
#         return self.name

# # Create the UserProfile model to extend the built-in User model
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

#     def __str__(self):
#         return f"{self.user.username}'s Profile"

# # Signal handler to automatically create a UserProfile when a new User is created
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# # Signal handler to save the UserProfile whenever the User object is saved
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()

# from django.db import models

# class Library(models.Model):
#     name = models.CharField(max_length=200)
#     location = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=200)
#     isbn = models.CharField(max_length=13, unique=True)
#     library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='books')

#     # Define custom permissions for the Book model
#     class Meta:
#         permissions = [
#             ("can_add_book", "Can add a book entry"),
#             ("can_change_book", "Can edit a book entry"),
#             ("can_delete_book", "Can delete a book entry"),
#         ]

#     def __str__(self):
#         return f"{self.title} by {self.author}"

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

# from django.db import models

# class Library(models.Model):
#     name = models.CharField(max_length=200)
#     location = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=200)
#     isbn = models.CharField(max_length=13, unique=True)
#     library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='books')

#     # Define custom permissions for the Book model
#     class Meta:
#         permissions = [
#             ("can_add_book", "Can add a book entry"),
#             ("can_change_book", "Can edit a book entry"),
#             ("can_delete_book", "Can delete a book entry"),
#         ]

#     def __str__(self):
#         return f"{self.title} by {self.author}"

# from django.db import models

# class Library(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.name} located at {self.location}"

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)
#     isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
#     library = models.ForeignKey(Library, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return f"{self.title} by {self.author}"
    
# class Meta:
#     permissions = [
#       ("can_add_library", "Can add library"),
#     ] 

from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        permissions = [
            ("can_add_library", "Can add a new library"),
            # Add other custom library permissions here if needed
        ]

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_change_book", "Can change existing book data"),
            ("can_delete_book", "Can delete a book"),
        ]

    def __str__(self):
        return self.title
