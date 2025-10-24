# # accounts/urls.py

# from django.urls import path
# from .views import (
#     UserRegistrationView, 
#     CustomAuthToken, 
#     UserProfileView,
#     PublicUserProfileView,
#     FollowUserView
# )

# # Define the app name for namespacing
# app_name = 'accounts'

# urlpatterns = [
#     # --- Authentication Endpoints ---
    
#     # POST: Register a new user
#     path('auth/register/', UserRegistrationView.as_view(), name='register'),
    
#     # POST: Login and get token/user data (Overrides DRF's default login)
#     path('auth/login/', CustomAuthToken.as_view(), name='login'),
    
    
#     # --- Profile Endpoints ---
    
#     # GET/PUT/PATCH: Retrieve and update the currently authenticated user's profile
#     path('profile/', UserProfileView.as_view(), name='my_profile'),
    
#     # GET: Retrieve a public user profile by username
#     path('<str:username>/', PublicUserProfileView.as_view(), name='public_profile'),
    
#     # POST/DELETE: Follow or unfollow a user by username
#     path('<str:username>/follow/', FollowUserView.as_view(), name='follow_unfollow'),
# ]

from django.urls import path

from .views import (
    RegistrationView,  # Corrected from UserRegistrationView
    LoginView,
    UserProfileView,
    UserPublicProfileView
)

urlpatterns = [
    # Authentication Endpoints
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    # Profile Endpoints
    # The authenticated user's profile (access with token)
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    
    # Public profile (access by username)
    path('<str:username>/', UserPublicProfileView.as_view(), name='public-profile'),
]
