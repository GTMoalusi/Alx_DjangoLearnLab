from rest_framework import generics, permissions, serializers
from django.shortcuts import get_object_or_404

# IMPORTANT: In a real project, replace these placeholder imports 
# with the actual imports for your Post model and CustomUser model.
# Note: The Post model is now assumed to have a 'author' ForeignKey field.
# from .models import Post
# from accounts.models import CustomUser 
# ------------------------------------------------------------------

# --- Placeholders for Post and CustomUser for the purpose of the snippet ---
# Assuming 'Post' model has fields: author (ForeignKey to CustomUser), content, created_at
# Assuming 'CustomUser' model has a ManyToManyField: following
class Post:
    objects = None # Manager placeholder

# ------------------------------------------------------------------


# 1. Post Serializer
class PostSerializer(serializers.ModelSerializer): 
    """
    Serializer for the Post model, including the author's username.
    """
    # NOTE: Using 'author.username' based on the implied 'author' field.
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        # Replace Post with your actual Post model import
        # model = Post 
        # Temporarily using Serializer as Model is a placeholder
        fields = ('id', 'author_username', 'content', 'created_at')
        read_only_fields = ('author_username', 'created_at')


# 2. Feed View
class PostFeedView(generics.ListAPIView):
    """
    Generates a feed of posts from users that the current user follows.
    Posts are ordered by creation date (most recent first).
    Requires authentication.
    """
    # REQUIRED: Ensures only authenticated users can access the feed
    permission_classes = [permissions.IsAuthenticated] 
    serializer_class = PostSerializer
    
    def get_queryset(self):
        user = self.request.user

        # Get the queryset of User objects that the current user is following.
        following_users = user.following.all()
        
        # Filter posts where the author is in the set of following_users.
        # Posts are ordered by created_at descending (most recent first).
        queryset = Post.objects.filter(
            author__in=following_users
        ).order_by(
            '-created_at'
        )

        return queryset
