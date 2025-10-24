from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthorSerializer(serializers.ModelSerializer):
    """Minimal serializer for nested Author representation."""
    class Meta:
        model = User
        fields = ('id', 'username')


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for the Comment model."""
    # Use the minimal AuthorSerializer for the author field
    author = AuthorSerializer(read_only=True) 

    class Meta:
        model = Comment
        # Expose all fields including post ID, which is needed for nested URL logic
        fields = ('id', 'post', 'author', 'content', 'created_at', 'updated_at')
        # Mark 'post' as read-only, as it will be set by the ViewSet context
        read_only_fields = ('post', 'author') 

    def create(self, validated_data):
        """
        Sets the author to the currently logged-in user and saves the comment.
        The 'post' field is injected from the ViewSet's perform_create method.
        """
        validated_data['author'] = self.context['request'].user
        return Comment.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the Post model."""
    # Use the minimal AuthorSerializer for the author field
    author = AuthorSerializer(read_only=True) 
    
    # Read-only field to display the count of comments
    comment_count = serializers.SerializerMethodField()
    
    # Hyperlink to the detail view (assuming 'post-detail' name is used in URLs)
    url = serializers.HyperlinkedIdentityField(view_name='post-detail', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'url', 'author', 'title', 'content', 'comment_count', 'created_at', 'updated_at')
        read_only_fields = ('author',) # Author is set automatically

    def get_comment_count(self, obj):
        """Returns the number of comments associated with the post."""
        # The related_name 'comments' on the Post model is used here
        return obj.comments.count()

    def create(self, validated_data):
        """Sets the author to the currently logged-in user before creating the post."""
        validated_data['author'] = self.context['request'].user
        return Post.objects.create(**validated_data)
