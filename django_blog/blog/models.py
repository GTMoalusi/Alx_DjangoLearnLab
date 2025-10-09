from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Model representing a single blog post.
    """
    # Required Fields
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    # ForeignKey to Django's built-in User model
    # CASCADE means if the User is deleted, all their posts are also deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Optional field for better user experience
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    class Meta:
        ordering = ['-published_date'] # Order posts from newest to oldest

    def __str__(self):
        return self.title