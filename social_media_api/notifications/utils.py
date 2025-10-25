from django.contrib.contenttypes.models import ContentType
from .models import Notification

def create_notification(recipient, actor, verb, target):
    """
    Creates a new Notification instance.
    
    Args:
        recipient (User): The user who will receive the notification.
        actor (User): The user who performed the action.
        verb (str): The action verb (e.g., 'liked', 'followed').
        target (Model instance): The object the action was performed on (e.g., Post).
    """
    # Ensure the recipient is not the actor (don't notify a user of their own actions)
    if recipient == actor:
        return

    # Get the ContentType for the target object
    target_content_type = ContentType.objects.get_for_model(target)

    # Create the notification
    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        content_type=target_content_type,
        object_id=target.pk,
        target=target
    )
    # Note: We don't return anything, just ensure creation.
