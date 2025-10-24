from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

# Create a router and register the PostViewSet with it.
# This automatically generates /posts/ and /posts/{pk}/ endpoints.
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# Define urlpatterns
urlpatterns = [
    # 1. Include the router-generated URLs for Posts
    path('', include(router.urls)),
    
    # 2. Nested URLs for Comments (Manually defined)
    # -----------------------------------------------
    
    # Route for listing and creating comments for a specific post:
    # URL: /posts/{post_pk}/comments/
    path('posts/<int:post_pk>/comments/', 
         CommentViewSet.as_view({
             'get': 'list',   # GET /posts/1/comments/
             'post': 'create' # POST /posts/1/comments/
         }), 
         name='comment-list'),
    
    # Route for retrieving, updating, and deleting a specific comment:
    # URL: /posts/{post_pk}/comments/{pk}/
    path('posts/<int:post_pk>/comments/<int:pk>/', 
         CommentViewSet.as_view({
             'get': 'retrieve',       # GET /posts/1/comments/5/
             'put': 'update',         # PUT /posts/1/comments/5/
             'patch': 'partial_update', # PATCH /posts/1/comments/5/
             'delete': 'destroy'      # DELETE /posts/1/comments/5/
         }), 
         name='comment-detail'),
]
