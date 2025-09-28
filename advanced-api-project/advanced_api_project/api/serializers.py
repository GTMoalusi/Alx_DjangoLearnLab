# api/serializers.py
from rest_framework import serializers
from .models import ProjectItem

class ProjectItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProjectItem model.
    
    This handles converting ProjectItem instances to JSON format 
    and validates incoming data for creating/updating items.
    """
    
    class Meta:
        # The model that this serializer is based on
        model = ProjectItem
        
        # List all fields from the model you want to include in the API response
        # These fields will be available for both reading and writing (unless specified otherwise)
        fields = [
            'id', 
            'title', 
            'description', 
            'status', 
            'created_at', 
            'updated_at'
        ]
        
        # These fields are included in the output but cannot be set or updated 
        # via an API request (DRF handles the auto_now/auto_now_add for us)
        read_only_fields = ['created_at', 'updated_at']
