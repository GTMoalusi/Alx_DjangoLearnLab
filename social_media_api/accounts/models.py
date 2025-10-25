from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model extending Django's built-in AbstractUser.
    Includes a self-referential ManyToMany field for following/followers.
    """
    
    # The M2M field for following relationships.
    # 'self' points back to CustomUser.
    # symmetrical=False means following is one-directional (A follows B, B doesn't automatically follow A).
    following = models.ManyToManyField(
        'self',
        related_name='followers',
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.username
