# # # accounts/models.py

# # from django.db import models
# # from django.contrib.auth.models import AbstractUser

# # class User(AbstractUser):
# #     """
# #     Custom User model extending Django's AbstractUser.
    
# #     This model includes social media specific fields:
# #     1. bio: A short biography or status.
# #     2. profile_picture: An optional user profile image.
# #     3. followers: A ManyToMany relationship to itself for tracking follows.
# #     """
# #     # 1. User Bio (optional text field)
# #     bio = models.TextField(
# #         max_length=500, 
# #         blank=True, 
# #         null=True,
# #         verbose_name="Biography"
# #     )
    
# #     # 2. Profile Picture (optional image field)
# #     # NOTE: Requires the 'Pillow' library for image handling (pip install Pillow)
# #     profile_picture = models.ImageField(
# #         upload_to='profile_pics/', 
# #         blank=True, 
# #         null=True,
# #         verbose_name="Profile Picture"
# #     )
    
# #     # 3. Followers (Many-to-Many self-referential field)
# #     followers = models.ManyToManyField(
# #         'self', 
# #         # Defines the reverse relationship name (i.e., the users *this* user is following)
# #         related_name='following', 
# #         # symmetrical=False means the following is one-way (A follows B, B doesn't automatically follow A)
# #         symmetrical=False,
# #         blank=True
# #     )

# #     class Meta:
# #         # Define the default ordering for User lookups
# #         ordering = ('username',)

# #     def __str__(self):
# #         # Use the username as the primary string representation
# #         return self.username

# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     # The 'following' field is a Many-to-Many relationship to itself.
#     # It represents all the CustomUser instances that THIS user is following.
#     following = models.ManyToManyField(
#         'self', 
#         symmetrical=False, 
#         related_name='followers',
#         blank=True
#     )
    
#     # You can add other custom fields here later if needed (e.g., bio, profile_picture)

#     def __str__(self):
#         return self.username

#     def follow(self, user_to_follow):
#         """Adds a user to this user's following list."""
#         if user_to_follow != self:
#             self.following.add(user_to_follow)

#     def unfollow(self, user_to_unfollow):
#         """Removes a user from this user's following list."""
#         self.following.remove(user_to_unfollow)

#     def is_following(self, user):
#         """Checks if this user is following another user."""
#         return self.following.filter(pk=user.pk).exists()

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# CRITICAL: The class MUST be named CustomUser to match the lazy reference
# 'accounts.CustomUser' found in settings.AUTH_USER_MODEL and in your migrations.
class CustomUser(AbstractUser):
    """
    A custom user model inheriting from Django's AbstractUser.
    Includes fields and methods for handling social media following relationships.
    """

    # Many-to-Many field for followers. This is a self-referential relationship.
    # The related_name 'following' allows us to easily find who this user follows:
    # user_a.following.all() -> all users that user_a follows
    # user_b.followers.all() -> all users who follow user_b
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,  # References the user model itself (accounts.CustomUser)
        symmetrical=False,         # Important: Following is one-way
        related_name='following',
        blank=True,
    )

    # --- Follow Management Helper Methods ---

    def follow(self, user_to_follow):
        """Adds a user to the current user's set of followed users."""
        if user_to_follow != self:
            self.following.add(user_to_follow)

    def unfollow(self, user_to_unfollow):
        """Removes a user from the current user's set of followed users."""
        self.following.remove(user_to_unfollow)

    def is_following(self, user_to_check):
        """Checks if the current user is following the user_to_check."""
        return self.following.filter(pk=user_to_check.pk).exists()
    
    def __str__(self):
        return self.username
