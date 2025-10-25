from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class Notification(models.Model):
    """
    Model for tracking user notifications (likes, followers, comments, etc.).
    Uses GenericForeignKey for flexible targeting of objects (Post, Comment, etc.).
    """
    # The user who should receive the notification
    recipient = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='notifications',
        help_text="The user who receives the notification."
    )
    
    # The user who performed the action (e.g., liked the post, followed)
    actor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='actions_made',
        help_text="The user who initiated the action."
    )
    
    # A short phrase describing the action (e.g., 'liked', 'followed', 'commented')
    verb = models.CharField(max_length=255, db_index=True)
    
    # Generic Foreign Key setup to link to any Django model
    content_type = models.ForeignKey(
        ContentType, 
        on_delete=models.CASCADE,
        related_name='target_notifications',
        help_text="The type of object the action was performed on (e.g., 'Post')."
    )
    object_id = models.PositiveIntegerField(
        db_index=True,
        help_text="The primary key of the target object."
    )
    # The actual target object (Post, Comment, etc.)
    target = GenericForeignKey('content_type', 'object_id')
    
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.actor.username} {self.verb} {self.target} (to {self.recipient.username})"
