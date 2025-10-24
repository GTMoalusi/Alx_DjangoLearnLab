from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import CustomUser

class FollowUnfollowView(APIView):
    """
    Handles both follow and unfollow actions using a single POST endpoint.
    - If the current user is NOT following the target user (pk), it initiates a follow.
    - If the current user IS following the target user (pk), it initiates an unfollow.
    Requires authentication.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, format=None):
        """
        Toggles the follow status between the requesting user and the target user.
        """
        try:
            # 1. Get the target user (the one being followed/unfollowed)
            user_to_modify = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # 2. Get the user performing the action (current authenticated user)
        current_user = request.user

        # Safety check: Prevent self-follow
        if user_to_modify == current_user:
            return Response({"detail": "You cannot follow or unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # 3. Toggle logic
        if current_user.is_following(user_to_modify):
            # Already following, so unfollow
            current_user.unfollow(user_to_modify)
            message = f"Successfully unfollowed {user_to_modify.username}."
        else:
            # Not following, so follow
            current_user.follow(user_to_modify)
            message = f"Successfully followed {user_to_modify.username}."

        return Response({"detail": message, "is_following": not current_user.is_following(user_to_modify)}, status=status.HTTP_200_OK)
