from django.urls import path
from . import views

# Define the namespace for use in templates (e.g., href="{% url 'blog:post_list' %}")
app_name = 'blog'

urlpatterns = [
    # Post List and Creation
    path('', views.PostListView.as_view(), name='post_list'),
    path('new/', views.PostCreateView.as_view(), name='post_create'),
    
    # Search Feature
    path('search/', views.PostSearchView.as_view(), name='post_search'),

    # --- New: Tag Filtering Feature ---
    # URL to display posts associated with a specific tag (e.g., /tags/python/)
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='post_by_tag'),
    # -----------------------------------

    # Post Detail, Update, and Delete (using slug for human-readable URLs)
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Comment Creation (Post Slug is used to identify the parent post)
    path('posts/<slug:slug>/comment/new/', views.CommentCreateView.as_view(), name='comment_create'),
    
    # Comment Update and Delete (using the Comment's primary key (pk) for identification)
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]
