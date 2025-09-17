# users/models.py

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

# Define a custom manager for the user model.
class CustomUserManager(BaseUserManager):
    """Define a model manager for CustomUser with no username field."""
    # Use_in_migrations is a Django feature that allows the manager to be serialized
    # and used in migrations.
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        # Ensure that an email address is provided.
        if not email:
            raise ValueError("The given email must be set")
        
        # Normalize the email address before saving.
        email = self.normalize_email(email)
        
        # Create a new user instance.
        user = self.model(email=email, **extra_fields)
        
        # Set the user's password.
        user.set_password(password)
        
        # Save the user to the database.
        user.save(using=self._db)
        
        # Return the created user.
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a non-superuser with the given email and password."""
        # Ensure that is_staff and is_superuser are set to False.
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        
        # Call the _create_user method to create the user.
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        # Ensure that is_staff and is_superuser are set to True.
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        # Raise an error if is_staff is False.
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        
        # Raise an error if is_superuser is False.
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        # Call the _create_user method to create the superuser.
        return self._create_user(email, password, **extra_fields)

# Define the custom user model.
class CustomUser(AbstractUser):
    """Custom user model."""
    # The email field is a unique identifier.
    email = models.EmailField(_("email address"), unique=True)
    
    # The username field is no longer required for authentication.
    # It is still needed for compatibility with the Django admin.
    username = models.CharField(max_length=150, unique=False)

    # Set the email field as the unique identifier for authentication.
    USERNAME_FIELD = "email"
    
    # Remove the email from the list of required fields.
    REQUIRED_FIELDS = ["username"]

    # Set the custom manager as the manager for this model.
    objects = CustomUserManager()

    def __str__(self):
        """Return a string representation of the user."""
        return self.username
