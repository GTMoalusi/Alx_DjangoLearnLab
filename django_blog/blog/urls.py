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
# We import the views module which contains the PostList and PostDetail classes
from . import views

# Set an application namespace
app_name = 'blog'

urlpatterns = [
    # URL for the list of all posts (Home Page)
    # The view is called PostList
    # path('', views.PostList.as_view(), name='post_list'),
    
    # URL for a single post detail view using the unique slug
    # The view is called PostDetail
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
