# # # from django.db import models

# # # # Create your models here.

# # # class ProjectItem(models.Model):
# # #     """
# # #     Represents a single item or task within a project.
# # #     """
# # #     # A short, descriptive name for the item
# # #     title = models.CharField(max_length=255)

# # #     # A detailed description of the task
# # #     description = models.TextField(blank=True, null=True)

# # #     # Status of the item (e.g., To Do, In Progress, Complete)
# # #     STATUS_CHOICES = [
# # #         ('TODO', 'To Do'),
# # #         ('INPR', 'In Progress'),
# # #         ('DONE', 'Done'),
# # #     ]
# # #     status = models.CharField(
# # #         max_length=4,
# # #         choices=STATUS_CHOICES,
# # #         default='TODO',
# # #     )

# # #     # Date and time the item was created
# # #     created_at = models.DateTimeField(auto_now_add=True)

# # #     # Date and time the item was last updated
# # #     updated_at = models.DateTimeField(auto_now=True)

# # #     def __str__(self):
# # #         """
# # #         String representation of the model instance, used by the Django Admin.
# # #         """
# # #         return f"[{self.get_status_display()}] {self.title}"

# # #     class Meta:
# # #         # Define the default sorting order for query results
# # #         ordering = ['created_at']
# # #         # Give the model a verbose, plural name for the Admin site
# # #         verbose_name_plural = "Project Items"

# # from django.db import models

# # class Author(models.Model):
# #     name = models.CharField(max_length=100)
# #     # This field is often required for custom serializer fields
# #     birth_date = models.DateField(null=True, blank=True) 

# #     def __str__(self):
# #         return self.name

# # class Book(models.Model):
# #     title = models.CharField(max_length=200)
# #     publication_date = models.DateField()
# #     author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
# #     # Assuming the check wants a specific field like isbn
# #     isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)

# #     def __str__(self):
# #         return f"{self.title} by {self.author.name}"

# from django.db import models

# class ProjectItem(models.Model):
#     """
#     A simple model representing an item or task within the project.
#     We are defining this model to resolve the ImportError.
#     """
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     completed = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         """String representation of the model for the Django Admin."""
#         return self.title

#     class Meta:
#         # Ensures that your models app is properly named in migrations
#         app_label = 'api'
#         ordering = ['-created_at']

# from django.db import models

# # Model 1: Project Item (The original model we defined)
# class ProjectItem(models.Model):
#     """
#     A simple model representing an item or task within the project.
#     """
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     completed = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         app_label = 'api'
#         ordering = ['-created_at']


# # Model 2: Author (Required by serializers.py)
# class Author(models.Model):
#     """
#     Model for a book author.
#     """
#     name = models.CharField(max_length=100)
#     birth_date = models.DateField(null=True, blank=True)

#     def __str__(self):
#         return self.name


# # Model 3: Book (Required by serializers.py)
# class Book(models.Model):
#     """
#     Model for a book, linked to an Author.
#     """
#     title = models.CharField(max_length=255)
#     # ForeignKey creates a one-to-many relationship: one Author can have many Books
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
#     publication_year = models.DateField()
#     isbn = models.CharField(max_length=13, unique=True)

#     def __str__(self):
#         return f"{self.title} by {self.author.name}"

# from django.db import models

# # Minimal model definitions required for serializers and views to work.
# # NOTE: The ForeignKey in Book uses related_name='books', as assumed by the serializer.

# class Author(models.Model):
#     """Represents a book author."""
#     name = models.CharField(max_length=200)
#     bio = models.TextField(blank=True)
#     date_of_birth = models.DateField(null=True, blank=True)

#     def __str__(self):
#         return self.name

# class Book(models.Model):
#     """Represents a published book."""
#     title = models.CharField(max_length=255)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
#     year_published = models.IntegerField()
#     isbn = models.CharField(max_length=13, unique=True)

#     def __str__(self):
#         return self.title

from django.db import models

class Book(models.Model):
    """
    Defines the Book model fields.
    This model is necessary for the API views and serializers to work.
    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.title
