from django.urls import path
from .views import FollowUserView, UnfollowUserView, UserDetailView

urlpatterns = [
    # API route to fetch a single user's details (profile data, counts, etc.)
    # Example usage: GET to /api/accounts/5/
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    
    # Route for following a user. 
    # Example usage: POST to /api/accounts/5/follow/ 
    path('<int:pk>/follow/', FollowUserView.as_view(), name='follow-user'),
    
    # Route for unfollowing a user.
    # Example usage: POST to /api/accounts/5/unfollow/ 
    path('<int:pk>/unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
]
