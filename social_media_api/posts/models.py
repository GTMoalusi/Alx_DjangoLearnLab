from django.db import models
# Import the helper function, NOT the model directly.
from django.contrib.auth import get_user_model 

# We call this function AFTER the settings have been loaded, 
# which avoids the circular import problem.
User = get_user_model()

class Post(models.Model):
    """
    A simple model for a social media post.
    """
    # Use the User object obtained from get_user_model()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        # Displaying the first 50 characters of the post content
        return f"Post by {self.author.username}: {self.content[:50]}..." 
