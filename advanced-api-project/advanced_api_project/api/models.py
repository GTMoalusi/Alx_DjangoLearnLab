from django.db import models

# Create your models here.

class ProjectItem(models.Model):
    """
    Represents a single item or task within a project.
    """
    # A short, descriptive name for the item
    title = models.CharField(max_length=255)

    # A detailed description of the task
    description = models.TextField(blank=True, null=True)

    # Status of the item (e.g., To Do, In Progress, Complete)
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('INPR', 'In Progress'),
        ('DONE', 'Done'),
    ]
    status = models.CharField(
        max_length=4,
        choices=STATUS_CHOICES,
        default='TODO',
    )

    # Date and time the item was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Date and time the item was last updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of the model instance, used by the Django Admin.
        """
        return f"[{self.get_status_display()}] {self.title}"

    class Meta:
        # Define the default sorting order for query results
        ordering = ['created_at']
        # Give the model a verbose, plural name for the Admin site
        verbose_name_plural = "Project Items"
