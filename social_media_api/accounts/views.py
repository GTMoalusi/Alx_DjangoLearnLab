from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser 
# Assuming you have a basic UserSerializer or will use one later; including it for standard practice.
# from .serializers import UserSerializer 

class FollowUserView(generics.GenericAPIView):
    """
    Allows an authenticated user to follow another user (specified by PK).
    Endpoint: POST to /api/v1/accounts/{pk}/follow/
    """
    # Exposes the user queryset for DRF routing and documentation
    queryset = CustomUser.objects.all() 
    # Ensures only logged-in users can perform this action
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        # Retrieve the user the current user wants to follow
        target_user = get_object_or_404(CustomUser, pk=pk)
        
        # Prevent self-following
        if target_user == request.user:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Use the CustomUser model's helper method to add the relationship
        request.user.follow(target_user)

        return Response(
            {"detail": f"Successfully followed {target_user.username}.", "is_following": True},
            status=status.HTTP_201_CREATED
        )

class UnfollowUserView(generics.GenericAPIView):
    """
    Allows an authenticated user to unfollow another user (specified by PK).
    Endpoint: POST to /api/v1/accounts/{pk}/unfollow/
    """
    # Exposes the user queryset for DRF routing and documentation
    queryset = CustomUser.objects.all()
    # Ensures only logged-in users can perform this action
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        # Retrieve the user the current user wants to unfollow
        target_user = get_object_or_404(CustomUser, pk=pk)

        # Prevent self-unfollowing
        if target_user == request.user:
            return Response(
                {"detail": "You cannot unfollow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Use the CustomUser model's helper method to remove the relationship
        request.user.unfollow(target_user)

        return Response(
            {"detail": f"Successfully unfollowed {target_user.username}.", "is_following": False},
            status=status.HTTP_200_OK
        )
