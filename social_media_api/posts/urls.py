from django.urls import path
from .views import PostFeedView, LikePostView, UnlikePostView, PostCreateView # Import new views

urlpatterns = [
    # Route for creating a new post
    path('', PostCreateView.as_view(), name='post-create'),
    
    # New route for the user's personalized feed/timeline.
    path('feed/', PostFeedView.as_view(), name='post-feed'),
    
    # Routes for liking and unliking a post
    path('<int:pk>/like/', LikePostView.as_view(), name='post-like'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='post-unlike'),
    
    # You would typically add other routes here for standard operations like:
    # path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
