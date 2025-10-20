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

# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# # 1. The Profile Model
# # This model holds custom user data (bio, profile picture) that is 
# # not stored directly on Django's built-in User model.
# class Profile(models.Model):
#     # One-to-one link to the built-in User model. 
#     # If the User is deleted, the Profile is also deleted (CASCADE).
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    
#     # Custom fields for the user profile
#     bio = models.TextField(max_length=500, blank=True, null=True, 
#                            verbose_name="Biography")
    
#     # Profile Picture field (requires 'Pillow' library to be installed: pip install Pillow)
#     profile_picture = models.ImageField(
#         default='default_profile.png', # A default image should be placed in your MEDIA_ROOT/profile_pics/
#         upload_to='profile_pics',      # Files will be stored in MEDIA_ROOT/profile_pics/
#         blank=True,
#         null=True
#     )

#     def __str__(self):
#         # A human-readable representation of the object
#         return f'{self.user.username} Profile'

# # --- Signals: Automatically create and save Profile when User is created ---

# # 2. Signal to create a Profile for a new User
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     # 'created' is a boolean flag that is True if a new record was created
#     if created:
#         Profile.objects.create(user=instance)

# # 3. Signal to save the Profile whenever the User object is saved
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     # This handler ensures the profile is saved when the user is updated (e.g., via the profile view)
#     # We check if 'profile' attribute exists before calling save, just in case
#     if hasattr(instance, 'profile'):
#         instance.profile.save()

# from django.db import models
# from django.contrib.auth import get_user_model
# from django.urls import reverse

# # Get the custom user model if defined, or use the default one
# User = get_user_model()

# class Post(models.Model):
#     """
#     Model representing a single blog post.
#     """
#     # Required Fields
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     published_date = models.DateTimeField(auto_now_add=True)
    
#     # Foreign Key to Django's built-in User model
#     # CASCADE means if the User is deleted, all their posts are also deleted.
#     author = models.ForeignKey(User, on_delete=models.CASCADE) 
    
#     # Optional field for better user experience
#     # slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

#     class Meta:
#         ordering = ['-published_date'] # Order posts from newest to oldest

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         """
#         Returns the URL to access a particular instance of the post.
#         This is required by Django's CreateView, UpdateView, and DeleteView.
#         """
#         return reverse('blog:post_detail', args=[str(self.pk)])

# # NOTE: I am commenting out the slug field for simplicity, as managing unique slugs
# # for every post creation/update requires more complex logic in the views/forms.

# from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse

# # --- Existing Post Model (Included for context and completeness) ---
# class Post(models.Model):
#     # Required Fields
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     published_date = models.DateTimeField(auto_now_add=True)

#     # Foreign Key to Django's built-in User model
#     # CASCADE means if the User is deleted, all their posts are also deleted.
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

#     # Optional field for better user experience
#     slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

#     class Meta:
#         ordering = ['-published_date']  # Order posts from newest to oldest

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         # We assume the post_detail URL takes the primary key (pk)
#         return reverse('blog:post_detail', kwargs={'pk': self.pk})

# # --- New Comment Model ---
# class Comment(models.Model):
#     # Foreign Key to Post: Many comments can belong to one post.
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
#     # Foreign Key to User: The user who authored the comment.
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     # Text field for the comment content
#     content = models.TextField()
    
#     # Timestamps
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         # Order comments by creation time (oldest first)
#         ordering = ['created_at']

#     def __str__(self):
#         # Display the author and the first 50 characters of the comment
#         return f"Comment by {self.author.username} on '{self.post.title}'"

#     def get_absolute_url(self):
#         # Redirect back to the post detail page after creation/update
#         return reverse('blog:post_detail', kwargs={'pk': self.post.pk})

from django.db import models
from django.contrib.auth.models import User # Import User model

class Post(models.Model):
    """
    Model representing a single blog post.
    """
    # Required Fields
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    # Foreign Key to Django's built-in User model
    # CASCADE means if the User is deleted, all their posts are also deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Optional field for better user experience
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    class Meta:
        ordering = ['-published_date'] # Order posts from newest to oldest

    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    Model representing a comment on a blog post.
    """
    # The post this comment belongs to (many-to-one relationship)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    # The user who wrote the comment
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # The actual content of the comment
    text = models.TextField(verbose_name='Your Comment')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Order comments with the oldest first (natural conversation flow)
        ordering = ['created_at'] 

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
