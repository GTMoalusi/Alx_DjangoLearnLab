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

# from django.db import models
# from django.contrib.auth.models import AbstractUser, UserManager
# from django.utils.translation import gettext_lazy as _

# class CustomUserManager(UserManager):
#     """
#     Custom user manager to handle the creation of users and superusers.
#     This is necessary to ensure the new fields are handled correctly.
#     """
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
        
#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractUser):
#     """
#     Custom User model extending Django's AbstractUser to add
#     `date_of_birth` and `profile_photo` fields.
#     """
#     date_of_birth = models.DateField(null=True, blank=True)
#     profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.username
