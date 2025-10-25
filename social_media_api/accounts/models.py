# from rest_framework import generics, permissions, status
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
# from .models import CustomUser  
# from .serializers import UserSerializer # Assuming you have a basic UserSerializer

# class FollowUserView(generics.GenericAPIView):
#     """
#     Allows an authenticated user to follow another user (specified by PK).
#     Uses the CustomUser model's helper method for logic encapsulation.
#     """
#     # Required for permission checks and documentation
#     queryset = CustomUser.objects.all() 
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, pk, *args, **kwargs):
#         # 1. Get the target user
#         target_user = get_object_or_404(CustomUser, pk=pk)
        
#         # 2. Validation
#         if target_user == request.user:
#             return Response(
#                 {"detail": "You cannot follow yourself."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        
#         # 3. Use the model's helper method
#         request.user.follow(target_user)

#         return Response(
#             {"detail": f"Successfully followed {target_user.username}.", "is_following": True},
#             status=status.HTTP_201_CREATED
#         )

# class UnfollowUserView(generics.GenericAPIView):
#     """
#     Allows an authenticated user to unfollow another user (specified by PK).
#     Uses the CustomUser model's helper method for logic encapsulation.
#     """
#     # Required for permission checks and documentation
#     queryset = CustomUser.objects.all()
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, pk, *args, **kwargs):
#         # 1. Get the target user
#         target_user = get_object_or_404(CustomUser, pk=pk)

#         # 2. Validation
#         if target_user == request.user:
#             return Response(
#                 {"detail": "You cannot unfollow yourself."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        
#         # 3. Use the model's helper method
#         # The method handles the database removal automatically.
#         request.user.unfollow(target_user)

#         return Response(
#             {"detail": f"Successfully unfollowed {target_user.username}.", "is_following": False},
#             status=status.HTTP_200_OK
#         )

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings # Crucial: Import settings to reference AUTH_USER_MODEL

class CustomUser(AbstractUser):
    """
    A custom user model extending AbstractUser.
    Includes the 'following' M2M relationship to track users being followed.
    """
    
    # M2M relationship: A user follows another user (self-referential).
    # Using settings.AUTH_USER_MODEL (a string reference) avoids the circular import 
    # when Django loads models and sets up migrations.
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='followers',
        symmetrical=False, # Following user A doesn't mean A follows you back
        blank=True,
    )

    def follow(self, user_to_follow):
        """Adds a user to the current user's following list."""
        if self != user_to_follow:
            self.following.add(user_to_follow)

    def unfollow(self, user_to_unfollow):
        """Removes a user from the current user's following list."""
        self.following.remove(user_to_unfollow)

    def is_following(self, user):
        """Checks if the current user is following the specified user."""
        return self.following.filter(pk=user.pk).exists()

    def __str__(self):
        return self.username
