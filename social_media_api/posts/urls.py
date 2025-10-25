from django.urls import path
from .views import PostFeedView

urlpatterns = [
    # New route for the user's personalized feed/timeline.
    # Example usage: GET to /api/posts/feed/
    path('feed/', PostFeedView.as_view(), name='post-feed'),
    
    # You would typically add other routes here for standard operations like:
    # path('', PostListCreateView.as_view(), name='post-list-create'),
    # path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
