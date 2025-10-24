# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    
    This model includes social media specific fields:
    1. bio: A short biography or status.
    2. profile_picture: An optional user profile image.
    3. followers: A ManyToMany relationship to itself for tracking follows.
    """
    # 1. User Bio (optional text field)
    bio = models.TextField(
        max_length=500, 
        blank=True, 
        null=True,
        verbose_name="Biography"
    )
    
    # 2. Profile Picture (optional image field)
    # NOTE: Requires the 'Pillow' library for image handling (pip install Pillow)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', 
        blank=True, 
        null=True,
        verbose_name="Profile Picture"
    )
    
    # 3. Followers (Many-to-Many self-referential field)
    followers = models.ManyToManyField(
        'self', 
        # Defines the reverse relationship name (i.e., the users *this* user is following)
        related_name='following', 
        # symmetrical=False means the following is one-way (A follows B, B doesn't automatically follow A)
        symmetrical=False,
        blank=True
    )

    class Meta:
        # Define the default ordering for User lookups
        ordering = ('username',)

    def __str__(self):
        # Use the username as the primary string representation
        return self.username
