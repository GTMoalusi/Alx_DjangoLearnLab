from rest_framework import serializers
from .models import Notification

# Helper Serializer for the Actor (User)
class ActorSerializer(serializers.Serializer):
    """Simple serializer to represent the actor (user) who triggered the notification."""
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=150)

# Helper Serializer for the Target (Post, Comment, etc.)
class TargetSerializer(serializers.Serializer):
    """
    Simple serializer to represent the target object (e.g., Post).
    Since we only have Posts/Users so far, we focus on a few common fields.
    """
    id = serializers.IntegerField()
    
    # Assuming 'content' field exists on the target (like Post model)
    content = serializers.CharField(max_length=200, required=False) 

class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Notification model.
    It uses helper serializers for the actor and the target object.
    """
    # Custom field for the actor (user who performed the action)
    actor = ActorSerializer(read_only=True)
    
    # Custom field to represent the target object (Post, Comment, etc.)
    # We use SerializerMethodField because GenericForeignKey cannot be serialized directly.
    target_info = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = (
            'id', 
            'actor', 
            'verb', 
            'target_info', 
            'timestamp', 
            'is_read'
        )
        read_only_fields = fields # All fields are read-only

    def get_target_info(self, obj):
        """
        Extracts relevant information from the GenericForeignKey target object.
        """
        if obj.target:
            # For simplicity, we assume the target is a Post (which has 'content')
            # In a full app, you would need logic here to handle different target models
            # (e.g., Post, Comment, Follow, etc.)
            
            # Use the TargetSerializer to format the object data
            return TargetSerializer(obj.target).data
            
        return None
