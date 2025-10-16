# from django.db import models
# from django.contrib.auth.models import User

# class Post(models.Model):
#     """
#     Model representing a single blog post.
#     """
#     # Required Fields
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     published_date = models.DateTimeField(auto_now_add=True)
    
#     # ForeignKey to Django's built-in User model
#     # CASCADE means if the User is deleted, all their posts are also deleted.
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     # Optional field for better user experience
#     slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

#     class Meta:
#         ordering = ['-published_date'] # Order posts from newest to oldest

#     def __str__(self):
#         return self.title

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# 1. The Profile Model
# This model holds custom user data (bio, profile picture) that is 
# not stored directly on Django's built-in User model.
class Profile(models.Model):
    # One-to-one link to the built-in User model. 
    # If the User is deleted, the Profile is also deleted (CASCADE).
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Custom fields for the user profile
    bio = models.TextField(max_length=500, blank=True, null=True, 
                           verbose_name="Biography")
    
    # Profile Picture field (requires 'Pillow' library to be installed: pip install Pillow)
    profile_picture = models.ImageField(
        default='default_profile.png', # A default image should be placed in your MEDIA_ROOT/profile_pics/
        upload_to='profile_pics',      # Files will be stored in MEDIA_ROOT/profile_pics/
        blank=True,
        null=True
    )

    def __str__(self):
        # A human-readable representation of the object
        return f'{self.user.username} Profile'

# --- Signals: Automatically create and save Profile when User is created ---

# 2. Signal to create a Profile for a new User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # 'created' is a boolean flag that is True if a new record was created
    if created:
        Profile.objects.create(user=instance)

# 3. Signal to save the Profile whenever the User object is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # This handler ensures the profile is saved when the user is updated (e.g., via the profile view)
    # We check if 'profile' attribute exists before calling save, just in case
    if hasattr(instance, 'profile'):
        instance.profile.save()
