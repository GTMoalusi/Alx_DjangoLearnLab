from django.db import models
from django.contrib.auth import get_user_model

# Get the custom User model defined in the accounts app
User = get_user_model()

class Post(models.Model):
    """
    Represents a social media post.
    """
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='posts',
        help_text="The user who created the post."
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] # Order posts by newest first

    def __str__(self):
        return f'{self.title} by {self.author.username}'

class Comment(models.Model):
    """
    Represents a comment on a post.
    """
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name='comments',
        help_text="The post this comment belongs to."
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments',
        help_text="The user who wrote the comment."
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at'] # Order comments by oldest first (chronological)

    def __str__(self):
        return f'Comment by {self.author.username} on Post ID {self.post.id}'
