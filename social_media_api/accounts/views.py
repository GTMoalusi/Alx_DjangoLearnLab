from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics # Provides GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated # Explicitly imported and used
from django.shortcuts import get_object_or_404
from rest_framework import serializers

# Assuming CustomUser is defined in the same application's models
from .models import CustomUser


# --- PLACEHOLDER: Normally defined in serializers.py ---
# This placeholder allows UserDetailView to run without a separate file.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # In a real app, you would include more fields
        fields = ['id', 'username', 'email'] 
# --------------------------------------------------------


# Refactored to use GenericAPIView and RetrieveModelMixin as requested.
class UserDetailView(RetrieveModelMixin, generics.GenericAPIView):
    """
    Retrieve details for a single user (viewing a profile).
    GET /accounts/{pk}/
    """
    # Uses the requested CustomUser.objects.all() via queryset
    queryset = CustomUser.objects.all() 
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    # Required method for RetrieveModelMixin
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class FollowUserView(APIView):
    """
    Allows an authenticated user to follow another user.
    POST /accounts/{pk}/follow/
    """
    permission_classes = [IsAuthenticated] # Used

    def post(self, request, pk):
        follower = request.user
        target_user = get_object_or_404(CustomUser, pk=pk)

        # Prevent following self
        if follower == target_user:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Execute the follow operation
        if not follower.following.filter(pk=target_user.pk).exists():
            follower.following.add(target_user)
            return Response(
                {"detail": f"Successfully followed {target_user.username}.",
                 "following_user_id": target_user.pk},
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            {"detail": f"You are already following {target_user.username}."},
            status=status.HTTP_400_BAD_REQUEST
        )


class UnfollowUserView(APIView):
    """
    Allows an authenticated user to unfollow another user.
    POST /accounts/{pk}/unfollow/
    """
    permission_classes = [IsAuthenticated] # Used

    def post(self, request, pk):
        unfollower = request.user
        target_user = get_object_or_404(CustomUser, pk=pk)

        # Prevent unfollowing self
        if unfollower == target_user:
            return Response(
                {"detail": "You cannot unfollow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Execute the unfollow operation
        if unfollower.following.filter(pk=target_user.pk).exists():
            unfollower.following.remove(target_user)
            return Response(
                {"detail": f"Successfully unfollowed {target_user.username}.",
                 "unfollowed_user_id": target_user.pk},
                status=status.HTTP_200_OK
            )
        
        return Response(
            {"detail": f"You are not currently following {target_user.username}."},
            status=status.HTTP_400_BAD_REQUEST
        )
