from django.urls import path
from .views import UserDetailView, FollowUserView, UnfollowUserView

# Namespace for this app's URLs
app_name = 'accounts'

urlpatterns = [
    # GET /accounts/{pk}/ - Retrieve user details (e.g., profile view)
    path(
        '<int:pk>/',
        UserDetailView.as_view(),
        name='user-detail'
    ),

    # POST /accounts/{pk}/follow/ - Follow a user
    path(
        '<int:pk>/follow/',
        FollowUserView.as_view(),
        name='user-follow'
    ),

    # POST /accounts/{pk}/unfollow/ - Unfollow a user
    path(
        '<int:pk>/unfollow/',
        UnfollowUserView.as_view(),
        name='user-unfollow'
    ),
]
