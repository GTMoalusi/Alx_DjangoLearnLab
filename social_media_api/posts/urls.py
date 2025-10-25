from django.urls import path
from .views import UserFeedView

urlpatterns = [
    # Path for the main user feed, using the view we defined earlier
    path('feed/', UserFeedView.as_view(), name='user_feed'),
]
