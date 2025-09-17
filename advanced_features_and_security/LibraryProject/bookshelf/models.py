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

# from django.db import models

# # Define the Library model first, as it's a foreign key for Book
# class Library(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# class Book(models.Model):
#    title = models.CharField(max_length= 200)
#    author = models.CharField(max_length= 100)
#    # Ensure these fields are present in your model
#    publication_year = models.IntegerField(null=True, blank=True)
#    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
#    # Add the Foreign Key relationship to Library
#    library = models.ForeignKey(Library, on_delete=models.SET_NULL, null=True)

#    def __str__(self):
#        return f"{self.title} by {self.author}"

#    class Meta:
#        permissions = [
#            ("can_add_book", "Can add a new book"),
#            ("can_change_book", "Can change an existing book"),
#            ("can_delete_book", "Can delete a book"),
#        ]

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

# from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)
#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")
#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField("email address", unique=True)
    
#     objects = CustomUserManager()

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email

# from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager

# # This is the CustomUser model we added earlier.
# class CustomUserManager(BaseUserManager):
#     """
#     Custom user model manager where email is the unique identifier
#     for authentication instead of usernames.
#     """
#     def create_user(self, email, password=None, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         """
#         Creates and saves a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")
#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField("email address", unique=True)
    
#     # Add related_name to avoid clashes with the default User model
#     groups = models.ManyToManyField(
#         "auth.Group",
#         related_name="custom_user_groups",
#         blank=True,
#     )
#     user_permissions = models.ManyToManyField(
#         "auth.Permission",
#         related_name="custom_user_permissions",
#         blank=True,
#     )

#     objects = CustomUserManager()

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email

# # Add the Book model that the relationship_app depends on
# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title

# # Add the Library model that the relationship_app depends on
# class Library(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# from django.db import models

# # The Book model that the relationship_app depends on
# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title

# # The Library model that the relationship_app depends on
# class Library(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# from django.db import models
# from django.conf import settings
# from django.contrib.auth.models import UserManager, AbstractUser

# class CustomUserManager(UserManager):
#     pass

# class CustomUser(AbstractUser):
#     objects = CustomUserManager()

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)
#     publication_year = models.IntegerField(blank=True, null=True)

#     class Meta:
#         # Define custom permissions for this model
#         permissions = (
#             ("can_view", "Can view book"),
#             ("can_create", "Can create book"),
#             ("can_edit", "Can edit book"),
#             ("can_delete", "Can delete book"),
#         )
#         # To avoid name conflicts, these are automatically prefixed with the app name,
#         # so you will reference them as 'bookshelf.can_view', 'bookshelf.can_create', etc.

#     def __str__(self):
#         return self.title

from django.db import models
from django.conf import settings
from django.contrib.auth.models import UserManager, AbstractUser

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(blank=True, null=True)

    class Meta:
        # Define custom permissions for this model
        permissions = (
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        )
        # To avoid name conflicts, these are automatically prefixed with the app name,
        # so you will reference them as 'bookshelf.can_view', 'bookshelf.can_create', etc.

    def __str__(self):
        return self.title

# This model has been added back to fix the ImportError
class Library(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
