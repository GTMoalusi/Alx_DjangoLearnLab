from rest_framework import generics, permissions, serializers
from django.shortcuts import get_object_or_404

# IMPORTANT: In a real project, replace these placeholder imports 
# with the actual imports for your Post model and CustomUser model.
# from .models import Post
# from accounts.models import CustomUser 
# ------------------------------------------------------------------

# --- Placeholders for Post and CustomUser for the purpose of the snippet ---
# Assuming 'Post' model has fields: user (ForeignKey to CustomUser), content, created_at
# Assuming 'CustomUser' model has a ManyToManyField: following
class Post:
    objects = None # Manager placeholder

# ------------------------------------------------------------------


# 1. Post Serializer
class PostSerializer(serializers.ModelSerializer): 
    """
    Serializer for the Post model, including the author's username.
    """
    # Assuming 'user' is a ForeignKey to CustomUser
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        # Replace Post with your actual Post model import
        # model = Post 
        # Temporarily using Serializer as Model is a placeholder
        fields = ('id', 'user_username', 'content', 'created_at')
        read_only_fields = ('user_username', 'created_at')


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
        # 1. Get the current authenticated user
        user = self.request.user

        # 2. Get the IDs of all users the current user is following.
        #    .all() returns the queryset of users the current user follows.
        followed_users_ids = user.following.all().values_list('id', flat=True)
        
        # 3. Combine the followed users' IDs with the current user's ID
        #    to ensure the user sees their own posts in the feed (common behavior).
        all_relevant_user_ids = list(followed_users_ids) + [user.id]
        
        # 4. Filter posts and order them
        queryset = Post.objects.filter(
            # Filter posts where the author (user__id) is one of the relevant IDs
            user__id__in=all_relevant_user_ids
        ).order_by(
            # Order by creation date, descending (most recent first)
            '-created_at'
        )

        return queryset
