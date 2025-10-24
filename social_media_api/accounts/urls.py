from django.urls import path
from .views import FollowUnfollowView
from .models import CustomUser

urlpatterns = [
    # Route for following/unfollowing a user: 
    # POST to /api/v1/accounts/follow/<user_pk>/
    # The 'pk' (primary key) in the URL pattern corresponds to the user 
    # that the requesting user wants to follow or unfollow.
    path('follow/<int:pk>/', FollowUnfollowView.as_view(), name='follow-unfollow'),
]
