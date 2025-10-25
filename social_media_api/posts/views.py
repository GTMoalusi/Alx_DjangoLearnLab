from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from posts.models import Post
from .serializers import PostSerializer
from rest_framework import status # Keeping status for consistency, even if not strictly used here
from rest_framework.response import Response # Keeping Response for consistency

class UserFeedView(ListAPIView):
    """
    API view to display a feed of posts from users the current user is following.
    The feed is ordered by creation date, showing the most recent posts at the top.
    """
    # Use the PostSerializer we created
    serializer_class = PostSerializer
    # Only authenticated users should be able to see their feed
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 1. Get the current authenticated user (request.user is available because of IsAuthenticated)
        user = self.request.user
        
        # 2. Get the list of users this user is following.
        # This assumes your CustomUser model has a ManyToMany field named 'following'.
        following_users = user.following.all()
        
        # 3. Filter posts:
        #    - author__in=following_users: Only include posts whose author is in the 'following_users' set.
        #    - order_by('-created_at'): Sort by created_at descending (most recent first).
        queryset = Post.objects.filter(author__in=following_users).order_by('-created_at')
        
        return queryset

# Note: You can add other post views (like PostCreateView, PostDetailView) here as needed.
