from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model.
    Only includes fields necessary for public display (e.g., in a post feed).
    """
    class Meta:
        model = CustomUser
        # We only need the ID and username for public representation
        fields = ('id', 'username',)
        read_only_fields = fields
