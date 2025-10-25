from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions 
from rest_framework import generics # NEW: Contains GenericAPIView
from rest_framework import serializers # NEW: Needed for the serializer

from django.shortcuts import get_object_or_404
from .models import CustomUser 
# Note: This assumes CustomUser has been properly defined in .models

# ----------------------------------------------------
# 1. Serializer for User Details
# ----------------------------------------------------
class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer to display basic user info and counts for profile views.
    Assumes the M2M relationship in CustomUser is defined as 'following'
    with a related_name='followers' on the reverse side.
    """
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'followers_count', 'following_count')
        
    def get_followers_count(self, obj):
        # Accesses the reverse relationship (who is following this user)
        # This assumes the related_name on the CustomUser.following field is 'followers'
        return obj.followers.count()

    def get_following_count(self, obj):
        # Accesses the users this user is following
        return obj.following.count()

# ----------------------------------------------------
# 2. User Profile Detail View (Uses Generics and required queryset)
# ----------------------------------------------------
class UserDetailView(generics.RetrieveAPIView):
    """
    Retrieves the details of a specific user, including followers/following counts.
    Uses generics.RetrieveAPIView (which inherits from generics.GenericAPIView).
    """
    # REQUIRED: Set the queryset to all CustomUser objects
    queryset = CustomUser.objects.all() 
    serializer_class = CustomUserSerializer


# ----------------------------------------------------
# 3. Follow/Unfollow Views (Existing)
# ----------------------------------------------------

class FollowUserView(APIView):
    """
    Allows the authenticated user to follow another user based on their ID (pk).
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        target_user = get_object_or_404(CustomUser, pk=pk)
        follower = request.user
        
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
            
        follower.following.add(target_user)
        
        return Response(
            {"detail": f"You are now following {target_user.username}."},
            status=status.HTTP_201_CREATED
        )

class UnfollowUserView(APIView):
    """
    Allows the authenticated user to unfollow another user based on their ID (pk).
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        target_user = get_object_or_404(CustomUser, pk=pk)
        unfollower = request.user
        
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
            
        unfollower.following.remove(target_user)
        
        return Response(
            {"detail": f"You have unfollowed {target_user.username}."},
            status=status.HTTP_200_OK
        )
