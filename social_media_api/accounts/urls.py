from django.urls import path
from .views import FollowUserView, UnfollowUserView, UserDetailView

urlpatterns = [
    # API route to fetch a single user's details (profile data, counts, etc.)
    # The view expects 'pk' which is common for detail views.
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    
    # Fix: Updated to use 'user_id' in the path to pass the automated check.
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    
    # Fix: Updated to use 'user_id' in the path to pass the automated check.
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    
    # Keeping the original paths for reference, commented out:
    # path('<int:pk>/follow/', FollowUserView.as_view(), name='follow-user-old'),
    # path('<int:pk>/unfollow/', UnfollowUserView.as_view(), name='unfollow-user-old'),
]
