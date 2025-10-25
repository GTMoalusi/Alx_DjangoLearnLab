from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """
    Extends Django's built-in AbstractUser to add custom fields.
    
    The 'following' field creates a social graph, allowing a user 
    to follow other users (a many-to-many relationship to itself).
    """
    # Inherits: username, first_name, last_name, email, is_staff, is_active, 
    # date_joined, etc., from AbstractUser.

    # Social graph field: A user follows many users, and is followed by many users.
    # 'self' refers back to the CustomUser model itself.
    following = models.ManyToManyField(
        'self',
        symmetrical=False, # Following is not reciprocal (A follows B, but B doesn't automatically follow A)
        related_name='followers', # The reverse relationship (who follows this user)
        blank=True
    )

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        # Use the username as the primary string representation
        return self.username
