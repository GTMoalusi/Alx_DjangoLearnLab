from django.urls import path
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    # Route for following a user. 
    # Example: POST /accounts/5/follow/ (to follow user with ID 5)
    path('<int:pk>/follow/', FollowUserView.as_view(), name='user-follow'),
    
    # Route for unfollowing a user.
    # Example: POST /accounts/5/unfollow/ (to unfollow user with ID 5)
    path('<int:pk>/unfollow/', UnfollowUserView.as_view(), name='user-unfollow'),
]

# Note: These URLs need to be included in your main project's urls.py 
# under a path like 'accounts/' or similar.
