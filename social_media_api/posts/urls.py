from django.urls import path
from .views import FeedView # Keep this import, as it is needed for the feed path

# The previous lines causing the error have been removed or commented out.
# Ensure you correctly import your other post views (like PostListCreateView/PostDetailView)
# from posts.views when you implement them.

urlpatterns = [
    # API endpoint for the personalized user feed
    path('feed/', FeedView.as_view(), name='user-feed'),
    
    # Placeholder for standard post paths:
    # path('', PostListCreateView.as_view(), name='post-list-create'),
    # path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
