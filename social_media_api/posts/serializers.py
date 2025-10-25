from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model, including the author's username and like count.
    """
    # ReadOnlyField to display the username of the author
    author_username = serializers.ReadOnlyField(source='author.username')
    # Custom field to calculate the number of likes on a post
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author_username', 'content', 'created_at', 'likes_count']
        read_only_fields = ['id', 'author_username', 'created_at', 'likes_count']

    def get_likes_count(self, obj):
        # Assumes the Post model has a related_name='likes' on the Like FK
        return obj.likes.count() 
