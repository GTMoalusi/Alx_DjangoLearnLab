from django.urls import path
from .views import UserFeedView

urlpatterns = [
    # Route for the user's customized feed
    path('feed/', UserFeedView.as_view(), name='user-feed'),

    # You would typically add other routes here, such as:
    # path('', PostListCreateView.as_view(), name='post-list-create'),
    # path('<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
]
