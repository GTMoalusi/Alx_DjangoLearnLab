# accounts/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import RegisterSerializer, UserProfileSerializer

# Get the custom User model
User = get_user_model()


# --- Authentication Views ---

class UserRegistrationView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    - Uses RegisterSerializer for validation and user/token creation.
    - Allows unauthenticated access (AllowAny).
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    
    def create(self, request, *args, **kwargs):
        """
        Overrides the default create method to return the user data and token 
        upon successful registration.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Call the serializer's create method, which handles user and token creation
        user = serializer.save() 
        
        # Get the token created in the serializer's create method
        token = Token.objects.get(user=user)

        # Prepare response data
        response_data = {
            "user": UserProfileSerializer(user).data, # Use the profile serializer to return clean user data
            "token": token.key,
            "message": "User registered successfully."
        }
        
        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


class CustomAuthToken(ObtainAuthToken):
    """
    Custom login view to override DRF's default ObtainAuthToken.
    It returns the user profile data along with the token upon successful login.
    """
    # Use DRF's default serializer (Username/Password fields)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        # Get or create the token
        token, created = Token.objects.get_or_create(user=user)
        
        # Return custom response format including user profile data
        return Response({
            'token': token.key,
            'user': UserProfileSerializer(user).data, # Include user data
            'message': 'Login successful.'
        })

# --- Profile Management Views ---

class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    API endpoint for viewing and updating the authenticated user's profile.
    - GET: Retrieve own profile.
    - PUT/PATCH: Update own profile (bio, profile_picture, names).
    - Requires authentication (IsAuthenticated).
    """
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_object(self):
        """
        Ensure the request is only retrieving/updating the profile of the 
        currently authenticated user.
        """
        return self.request.user

class PublicUserProfileView(generics.RetrieveAPIView):
    """
    API endpoint for viewing any user's profile based on their username.
    - Allows unauthenticated access (AllowAny) for viewing.
    """
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'username' # Look up the user by their unique username


# --- Follower/Following Views ---

class FollowUserView(generics.GenericAPIView):
    """
    API endpoint to follow/unfollow a user.
    - Expects 'username' in the URL path.
    - Requires authentication (IsAuthenticated).
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, username):
        """
        Endpoint for following a user.
        """
        # Get the user to be followed (the target)
        try:
            target_user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        # The user making the request (the follower)
        follower = request.user
        
        if follower == target_user:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if already following
        if follower.followers.filter(pk=target_user.pk).exists():
            return Response(
                {"detail": f"You are already following {username}."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # Perform the follow operation
        # Remember: follower.followers is the list of users the follower follows.
        follower.followers.add(target_user)
        
        return Response(
            {"detail": f"Successfully followed {username}.",
             "followers_count": target_user.following.count()}, # Target's new follower count
            status=status.HTTP_200_OK
        )

    def delete(self, request, username):
        """
        Endpoint for unfollowing a user.
        """
        try:
            target_user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."}, 
                status=status.HTTP_404_NOT_FOUND
            )
            
        follower = request.user

        if follower == target_user:
            return Response(
                {"detail": "Operation not permitted on yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if currently following
        if not follower.followers.filter(pk=target_user.pk).exists():
            return Response(
                {"detail": f"You are not currently following {username}."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # Perform the unfollow operation
        follower.followers.remove(target_user)
        
        return Response(
            {"detail": f"Successfully unfollowed {username}.",
             "followers_count": target_user.following.count()}, # Target's new follower count
            status=status.HTTP_200_OK
        )
