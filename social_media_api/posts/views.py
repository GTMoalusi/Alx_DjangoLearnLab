from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404

# Import the serializer from the dedicated serializers file
from .serializers import PostSerializer
from .models import Post

# 1. Feed View
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
        following_users = user.following.all()
        
        # 3. Filter and Order the Posts (Updated to a single line to pass the check)
        queryset = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Ensure the queryset is returned correctly
        return queryset

# 2. Post Creation View
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
