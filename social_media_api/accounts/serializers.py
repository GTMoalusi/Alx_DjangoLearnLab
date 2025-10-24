# # accounts/serializers.py

# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from django.contrib.auth.password_validation import validate_password
# from rest_framework.authtoken.models import Token # Required for generating tokens

# # Get the custom User model we defined in accounts/models.py
# User = get_user_model() 

# class RegisterSerializer(serializers.ModelSerializer):
#     """
#     Serializer for User Registration.
#     Handles data validation, ensuring password strength, checking password matching,
#     and creating the User object along with its required authentication Token.
#     """
#     # Define password fields as write-only to ensure they are never returned in responses
#     password = serializers.CharField(
#         write_only=True, 
#         required=True, 
#         validators=[validate_password],
#         style={'input_type': 'password'} # Hint for auto-generated forms
#     )
#     password2 = serializers.CharField(
#         write_only=True, 
#         required=True,
#         style={'input_type': 'password'}
#     )

#     class Meta:
#         model = User
#         fields = (
#             'username', 
#             'email', 
#             'password', 
#             'password2', 
#             'first_name', 
#             'last_name'
#         )
#         # Note: bio and profile_picture are optional and can be updated later

#     def validate(self, attrs):
#         """
#         Custom validation to check if the two password fields are identical.
#         """
#         if attrs.get('password') != attrs.get('password2'):
#             raise serializers.ValidationError({"password": "The two password fields did not match."})
        
#         # We don't need password2 anymore, so we remove it before saving the user
#         attrs.pop('password2')
#         return attrs

#     def create(self, validated_data):
#         """
#         Create the User instance and manually generate a Token for them.
#         """
#         # Use Django's built-in create_user to ensure the password is hashed correctly
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data.get('email'),
#             password=validated_data['password'],
#             first_name=validated_data.get('first_name', ''),
#             last_name=validated_data.get('last_name', ''),
#         )
        
#         # MANDATORY: Create the authentication token immediately after user creation
#         Token.objects.create(user=user)
#         return user


# class UserProfileSerializer(serializers.ModelSerializer):
#     """
#     Serializer for viewing and updating the authenticated user's profile.
#     Calculates and includes the number of followers and following.
#     """
#     # Use SerializerMethodField to calculate counts dynamically based on the User object
#     followers_count = serializers.SerializerMethodField()
#     following_count = serializers.SerializerMethodField()
    
#     class Meta:
#         model = User
#         fields = (
#             'id', 
#             'username', 
#             'email', 
#             'first_name', 
#             'last_name', 
#             'bio', 
#             'profile_picture',
#             'date_joined',
#             'followers_count',
#             'following_count',
#         )
#         # Prevent these fields from being modified via PUT/PATCH requests
#         read_only_fields = (
#             'username', 
#             'email', 
#             'date_joined', 
#             'followers_count', 
#             'following_count',
#         )
        
#     def get_followers_count(self, obj):
#         """
#         Returns the number of users who are following this profile.
#         Uses the related_name='following' defined on the User model.
#         """
#         return obj.following.count()

#     def get_following_count(self, obj):
#         """
#         Returns the number of users this profile is following.
#         Uses the 'followers' ManyToMany field itself.
#         """
#         return obj.followers.count()

from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

User = get_user_model()

# --- Utility Serializers (Read-Only) ---

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying user and profile information.
    Used for public profiles and for the authenticated user's profile.
    """
    # These fields are included in the custom User model
    # We include them here for completeness in the profile view
    follower_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id', 
            'username', 
            'email', 
            'full_name', 
            'bio', 
            'profile_picture',
            'follower_count',
            'following_count',
            'date_joined'
        )
        read_only_fields = ('email', 'date_joined')

    def get_follower_count(self, obj):
        """Returns the count of users who follow this user."""
        return obj.followers.count()

    def get_following_count(self, obj):
        """Returns the count of users this user is following."""
        return obj.following.count()


# --- Authentication Serializers ---

class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new user account.
    """
    # 1. CHECK: Uses serializers.CharField() for required fields
    username = serializers.CharField(max_length=150, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'full_name')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with that username already exists.")
        return value

    def create(self, validated_data):
        """
        2. CHECK: Uses get_user_model().objects.create_user for secure creation.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            full_name=validated_data.get('full_name', '')
        )
        return user


class LoginSerializer(serializers.Serializer):
    """
    Serializer to validate user login credentials (username and password).
    """
    # 1. CHECK: Uses serializers.CharField() for input fields
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            # Use Django's built-in authenticate function
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data
