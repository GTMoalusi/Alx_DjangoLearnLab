from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

# Assuming CustomUser is defined in the same application's models
from .models import CustomUser

class FollowUserView(APIView):
    """
    Allows an authenticated user to follow another user.
    POST /accounts/{pk}/follow/
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # The user initiating the follow action
        follower = request.user

        # The user being followed
        target_user = get_object_or_404(CustomUser, pk=pk)

        # Prevent following self
        if follower == target_user:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if already following to prevent duplicate records
        if follower.following.filter(pk=target_user.pk).exists():
            return Response(
                {"detail": f"You are already following {target_user.username}."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Execute the follow operation (assuming CustomUser has a 'following' ManyToMany field to 'self')
        follower.following.add(target_user)

        return Response(
            {"detail": f"Successfully followed {target_user.username}.",
             "following_user_id": target_user.pk},
            status=status.HTTP_201_CREATED
        )


class UnfollowUserView(APIView):
    """
    Allows an authenticated user to unfollow another user.
    POST /accounts/{pk}/unfollow/
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # The user initiating the unfollow action
        unfollower = request.user

        # The user being unfollowed
        target_user = get_object_or_404(CustomUser, pk=pk)

        # Prevent unfollowing self
        if unfollower == target_user:
            return Response(
                {"detail": "You cannot unfollow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if currently following
        if not unfollower.following.filter(pk=target_user.pk).exists():
            return Response(
                {"detail": f"You are not currently following {target_user.username}."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Execute the unfollow operation
        unfollower.following.remove(target_user)

        return Response(
            {"detail": f"Successfully unfollowed {target_user.username}.",
             "unfollowed_user_id": target_user.pk},
            status=status.HTTP_200_OK
        )
