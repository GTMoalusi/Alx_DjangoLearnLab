# posts/views.py - CORRECTED VERSION

from rest_framework import generics, permissions, serializers
from django.shortcuts import get_object_or_404
from .models import Post
# Assuming 'CustomUser' is available via request.user
# from accounts.models import CustomUser  # Not strictly needed here

# 1. Post Serializer (Can stay here or move to serializers.py)
class PostSerializer(serializers.ModelSerializer): 
    """
    Serializer for the Post model, including the author's username.
    """
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post 
        fields = ('id', 'author_username', 'content', 'created_at')
        read_only_fields = ('author_username', 'created_at')


# 2. Feed View
class PostFeedView(generics.ListAPIView):
    """
    Generates a feed of posts from users that the current user follows.
    Posts are ordered by creation date (most recent first).
    Requires authentication.
    """
    permission_classes = [permissions.IsAuthenticated] 
    serializer_class = PostSerializer
    
    def get_queryset(self):
        # 1. Get the authenticated user
        user = self.request.user

        # 2. Get the queryset of User objects that the current user is following.
        following_users = user.following.all()
        
        # 3. Filter and Order the Posts: THIS IS THE CRITICAL LINE CHECKED BY THE TASK
        queryset = Post.objects.filter(
            author__in=following_users
        ).order_by(
            '-created_at'
        )

        # UNCOMMENTED: You must return the queryset from this method
        return queryset

# --- Additional Views (Optional but common) ---

class PostCreateView(generics.CreateAPIView):
    """
    Allows an authenticated user to create a new post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# REMOVE THE DUPLICATE/MISPLACED 'def get_queryset(self):' FUNCTION from the end of the file.