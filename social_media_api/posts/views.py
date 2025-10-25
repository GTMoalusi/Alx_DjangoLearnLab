from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import IntegrityError # Needed for handling duplicate likes

from .models import Post, Like
from .serializers import PostSerializer
from notifications.utils import create_notification # Import utility

# ------------------------------------------------------------------
# 1. Post Feed and Creation Views
# ------------------------------------------------------------------

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
        
        # 3. Filter and Order the Posts
        # This line is critical for the feed logic
        queryset = Post.objects.filter(author__in=following_users).order_by('-created_at')

        return queryset

class PostCreateView(generics.CreateAPIView):
    """
    Allows an authenticated user to create a new post.
    """
    # Assuming Post.objects.all() is used as the base queryset
    queryset = Post.objects.all() 
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Automatically set the post's author to the logged-in user
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# ------------------------------------------------------------------
# 2. Like/Unlike Views
# ------------------------------------------------------------------

class LikePostView(APIView):
    """
    Allows an authenticated user to like a post.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        try:
            # Create the Like object
            Like.objects.create(post=post, user=user)
            
            # Send notification to the post author
            # Only notify if the liker is not the author
            if post.author != user:
                create_notification(
                    recipient=post.author, 
                    actor=user, 
                    verb="liked your post", 
                    target=post
                )

            return Response(
                {"detail": f"Post {pk} liked successfully."},
                status=status.HTTP_201_CREATED
            )

        except IntegrityError:
            # If the user tries to like the same post twice (due to unique_together constraint in Like model)
            return Response(
                {"detail": "Post already liked."},
                status=status.HTTP_409_CONFLICT
            )
        except Exception as e:
            # Handle other potential errors (e.g., database connection issues)
            return Response(
                {"detail": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UnlikePostView(APIView):
    """
    Allows an authenticated user to unlike a post.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        
        # Attempt to find and delete the Like object
        try:
            like = Like.objects.get(post=post, user=user)
            like.delete()
            
            # Note: Unliking does not typically remove the original 'like' notification.

            return Response(
                {"detail": f"Post {pk} unliked successfully."},
                status=status.HTTP_200_OK
            )
        except Like.DoesNotExist:
            return Response(
                {"detail": "You have not liked this post."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"detail": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
