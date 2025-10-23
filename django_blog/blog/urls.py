# from django.urls import path
# from .views import (
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView,
#     CommentCreateView,
#     CommentUpdateView,
#     CommentDeleteView,
# )

# # Define the application namespace
# app_name = 'blog'

# urlpatterns = [
#     # --- Post URLs ---
#     # List all posts
#     path('', PostListView.as_view(), name='post_list'),
    
#     # Create a new post
#     path('post/new/', PostCreateView.as_view(), name='post_create'),
    
#     # Detail view for a single post (uses both PK and Slug for SEO)
#     path('post/<int:pk>/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    
#     # Update an existing post
#     path('post/<int:pk>/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_update'),
    
#     # Delete an existing post
#     path('post/<int:pk>/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),

#     # --- Comment URLs (Updated to match specific check requirements) ---
    
#     # Create a new comment on a specific post (PK refers to the Post)
#     path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    
#     # Update an existing comment (PK refers to the Comment)
#     path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    
#     # Delete an existing comment (PK refers to the Comment)
#     path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    # TEMPORARILY COMMENTED OUT: This line is preventing makemigrations 
    # from running because PostList is not yet implemented or imported correctly in views.py
    # path('', views.PostList.as_view(), name='post_list'),
    
    # Add other implemented paths here if they exist, otherwise keep them commented out 
    # until you implement their corresponding views.
]