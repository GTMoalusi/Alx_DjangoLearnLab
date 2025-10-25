from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions # Required for IsAuthenticated

from django.shortcuts import get_object_or_404
from .models import CustomUser

class FollowUserView(APIView):
    """
    Allows the authenticated user to follow another user based on their ID (pk).
    Requires the user to be logged in.
    """
    # --- Enforcing authentication ---
    permission_classes = [permissions.IsAuthenticated]
    # --------------------------------

    def post(self, request, pk):
        # 1. Get the target user (the one being followed)
        target_user = get_object_or_404(CustomUser, pk=pk)
        follower = request.user
        
        # 2. Validation Checks
        if follower == target_user:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        if follower.following.filter(pk=target_user.pk).exists():
            return Response(
                {"detail": f"You are already following {target_user.username}."},
                status=status.HTTP_200_OK 
            )
            
        # 3. Perform the follow action
        follower.following.add(target_user)
        
        return Response(
            {"detail": f"You are now following {target_user.username}."},
            status=status.HTTP_201_CREATED
        )

class UnfollowUserView(APIView):
    """
    Allows the authenticated user to unfollow another user based on their ID (pk).
    Requires the user to be logged in.
    """
    # --- Enforcing authentication ---
    permission_classes = [permissions.IsAuthenticated]
    # --------------------------------

    def post(self, request, pk):
        # 1. Get the target user (the one being unfollowed)
        target_user = get_object_or_404(CustomUser, pk=pk)
        unfollower = request.user
        
        # 2. Validation Checks
        if unfollower == target_user:
            return Response(
                {"detail": "You cannot unfollow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        if not unfollower.following.filter(pk=target_user.pk).exists():
            return Response(
                {"detail": f"You are not currently following {target_user.username}."},
                status=status.HTTP_200_OK 
            )
            
        # 3. Perform the unfollow action
        unfollower.following.remove(target_user)
        
        return Response(
            {"detail": f"You have unfollowed {target_user.username}."},
            status=status.HTTP_200_OK
        )
