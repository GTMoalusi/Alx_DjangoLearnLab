from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model, including the author's username for easy display.
    """
    # ReadOnlyField to display the username of the author
    # This assumes the Post model has a ForeignKey called 'author'
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        # Include the new author_username field in the output
        fields = ['id', 'author_username', 'content', 'created_at']
        # Set fields that should not be modifiable via the API
        read_only_fields = ['id', 'author_username', 'created_at']
