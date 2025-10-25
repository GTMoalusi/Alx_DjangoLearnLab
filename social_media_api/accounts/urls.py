from django.urls import path
from .views import (
    UserDetailView,
    FollowUserView,
    UnfollowUserView
)

# Namespace for the app (optional but recommended)
app_name = 'accounts'

urlpatterns = [
    # Path for retrieving a single user's profile details (e.g., /accounts/1/)
    path(
        '<int:pk>/',
        UserDetailView.as_view(),
        name='user-detail'
    ),

    # Path for following a user (e.g., /accounts/1/follow/)
    path(
        '<int:pk>/follow/',
        FollowUserView.as_view(),
        name='user-follow'
    ),

    # Path for unfollowing a user (e.g., /accounts/1/unfollow/)
    path(
        '<int:pk>/unfollow/',
        UnfollowUserView.as_view(),
        name='user-unfollow'
    ),
]
