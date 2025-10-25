from django.urls import path
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    # POST /api/v1/accounts/{pk}/follow/
    # Allows the authenticated user to follow the user specified by 'pk'.
    path('<int:pk>/follow/', FollowUserView.as_view(), name='user-follow'),
    
    # POST /api/v1/accounts/{pk}/unfollow/
    # Allows the authenticated user to unfollow the user specified by 'pk'.
    path('<int:pk>/unfollow/', UnfollowUserView.as_view(), name='user-unfollow'),
    
    # Note: You would place other core account paths (registration, profile viewing, etc.) here.
]
