from django.urls import path
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    # Route for following a user. 
    # Example usage: POST to /api/accounts/5/follow/ (to follow user with ID 5)
    path('<int:pk>/follow/', FollowUserView.as_view(), name='follow-user'),
    
    # Route for unfollowing a user.
    # Example usage: POST to /api/accounts/5/unfollow/ (to unfollow user with ID 5)
    path('<int:pk>/unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
]
