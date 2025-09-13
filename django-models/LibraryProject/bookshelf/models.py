# from django.db import models

# # Create your models here.
# class Book(models.Model):
#    title = models.CharField(max_length= 200)
#    author = models.CharField(max_length= 100)
#    publication_year = models.IntegerField(null= True, blank= True)

# from django.db import models

# # Create your models here.
# class Book(models.Model):
#    title = models.CharField(max_length= 200)
#    author = models.CharField(max_length= 100)
#    publication_year = models.IntegerField(null= True, blank= True)

#    class Meta:
#        permissions = [
#            ("can_add_book", "Can add a new book"),
#            ("can_change_book", "Can change an existing book"),
#            ("can_delete_book", "Can delete a book"),
#        ]

# from django.db import models

# class Book(models.Model):
#    title = models.CharField(max_length= 200)
#    author = models.CharField(max_length= 100)
#    publication_year = models.IntegerField(null= True, blank= True)
#    # Add the new ISBN field to your model
#    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)

#    class Meta:
#        # Add the permissions back in
#        permissions = [
#            ("can_add_book", "Can add a new book"),
#            ("can_change_book", "Can change an existing book"),
#            ("can_delete_book", "Can delete a book"),
#        ]

# from django.db import models

# class Book(models.Model):
#    title = models.CharField(max_length= 200)
#    author = models.CharField(max_length= 100)
#    publication_year = models.IntegerField(null= True, blank= True)
#    # Add the ISBN field here
#    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
#    # Add the Library foreign key here
#    library = models.ForeignKey('Library', on_delete=models.SET_NULL, null=True)

#    def __str__(self):
#        return f"{self.title} by {self.author}"

#    class Meta:
#        # Add the permissions back in
#        permissions = [
#            ("can_add_book", "Can add a new book"),
#            ("can_change_book", "Can change an existing book"),
#            ("can_delete_book", "Can delete a book"),
#        ]

from django.db import models

# Define the Library model first, as it's a foreign key for Book
class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
   title = models.CharField(max_length= 200)
   author = models.CharField(max_length= 100)
   # Ensure these fields are present in your model
   publication_year = models.IntegerField(null=True, blank=True)
   isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
   # Add the Foreign Key relationship to Library
   library = models.ForeignKey(Library, on_delete=models.SET_NULL, null=True)

   def __str__(self):
       return f"{self.title} by {self.author}"

   class Meta:
       permissions = [
           ("can_add_book", "Can add a new book"),
           ("can_change_book", "Can change an existing book"),
           ("can_delete_book", "Can delete a book"),
       ]