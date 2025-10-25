# posts/views.py

from rest_framework import generics, permissions, serializers
from django.shortcuts import get_object_or_404

# IMPORTANT: Replace these placeholders with your actual model imports.
# Assuming 'Post' model is in the current app's 'models.py'
from .models import Post
# Assuming 'CustomUser' model is in the 'accounts' app
# from accounts.models import CustomUser 
# ------------------------------------------------------------------

# 1. Post Serializer
# NOTE: This serializer should typically be in a separate 'serializers.py' file,
# but is included here for completeness of the 'views.py' context.
class PostSerializer(serializers.ModelSerializer): 
    """
    Serializer for the Post model, including the author's username.
    """
    # Uses the author ForeignKey relationship to get the username
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post 
        # Fields available for reading/writing via the API
        fields = ('id', 'author_username', 'content', 'created_at')
        # Fields that can only be read, not set by the user during creation/update
        read_only_fields = ('author_username', 'created_at')


# 2. Feed View
class PostFeedView(generics.ListAPIView):
    """
    Generates a feed of posts from users that the current user follows.
    Posts are ordered by creation date (most recent first).
    Requires authentication.
    """
    # **Security**: Ensures only authenticated users can access the feed
    permission_classes = [permissions.IsAuthenticated] 
    serializer_class = PostSerializer
    
    def get_queryset(self):
        # 1. Get the authenticated user
        user = self.request.user

        # 2. Get the queryset of User objects that the current user is following.
        # This assumes your CustomUser model has a ManyToManyField named 'following' 
        # which links to other User objects.
        following_users = user.following.all()
        
        # 3. Filter and Order the Posts
        # Filter posts where the author is in the set of following_users,
        # and order them by created_at descending (most recent first).
        queryset = Post.objects.filter(
            author__in=following_users
        ).order_by(
            '-created_at'
        )

        return queryset

# --- Additional Views (Optional but common) ---

class PostCreateView(generics.CreateAPIView):
    """
    Allows an authenticated user to create a new post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Automatically set the post's author to the logged-in user
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)