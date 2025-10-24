# from rest_framework import viewsets, filters, permissions
# from rest_framework.pagination import PageNumberPagination
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import Post, Comment
# from .serializers import PostSerializer, CommentSerializer
# from .permissions import IsAuthorOrReadOnly # We will create this file next

# # --- Pagination Configuration (Step 5) ---

# class CustomPagination(PageNumberPagination):
#     """
#     Sets the page size for lists of posts to 10.
#     """
#     page_size = 10
#     page_size_query_param = 'page_size' # Allows user to override page size with ?page_size=X
#     max_page_size = 100


# # --- Post ViewSet (Steps 3 & 5) ---

# class PostViewSet(viewsets.ModelViewSet):
#     """
#     Provides full CRUD operations for Posts.
#     - Applies pagination.
#     - Allows filtering by author ID and searching by title/content.
#     - Ensures users are authenticated, and only the author can edit/delete.
#     """
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     pagination_class = CustomPagination
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)

#     # Filtering and Searching Backends
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    
#     # 1. DjangoFilterBackend: Filters posts by the 'author' ID
#     filterset_fields = ['author']
    
#     # 2. SearchFilter: Searches 'title' and 'content' for keywords
#     search_fields = ['title', 'content'] 
    
#     # 3. OrderingFilter: Allows ordering by fields like '-created_at' or 'title'
#     ordering_fields = ['created_at', 'updated_at', 'title']
#     ordering = ['-created_at'] # Default ordering (newest first)

#     def perform_create(self, serializer):
#         """
#         Automatically sets the author field to the current user when creating a new post.
#         The author is set here, not in the serializer, for simplicity and security.
#         """
#         serializer.save(author=self.request.user)


# # --- Comment ViewSet (Step 3) ---

# class CommentViewSet(viewsets.ModelViewSet):
#     """
#     Provides full CRUD operations for Comments.
#     - Only shows comments belonging to the post ID specified in the URL.
#     - Permissions ensure only the author can edit/delete their comment.
#     """
#     serializer_class = CommentSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)
    
#     def get_queryset(self):
#         """
#         This custom method filters the queryset to only include comments
#         for the Post specified in the URL via the 'post_pk' kwarg.
#         """
#         # The 'post_pk' keyword argument comes from the router's nested URL setup
#         post_pk = self.kwargs.get('post_pk')
#         if post_pk:
#             return Comment.objects.filter(post=post_pk)
#         return Comment.objects.all()

#     def perform_create(self, serializer):
#         """
#         Sets the comment's author to the current user and associates it 
#         with the correct Post based on the URL.
#         """
#         post_pk = self.kwargs.get('post_pk')
#         # We must use Post.objects.get() to ensure the post exists
#         post_instance = Post.objects.get(pk=post_pk)
        
#         # Save the comment, linking it to the current user and the post instance
#         serializer.save(author=self.request.user, post=post_instance)

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model

# --- PLACEHOLDER MODELS AND SERIALIZER ---
# NOTE: Please REPLACE these placeholder definitions with your actual imports 
# from posts.models and posts.serializers in your working environment.

class Post(models.Model):
    """
    Mock Post Model. In your real project, this is imported from `posts.models`.
    Assumes a ForeignKey relationship to the CustomUser model.
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        # Prevents Django from trying to create this mock table
        abstract = True 

class PostSerializer(serializers.ModelSerializer):
    """
    Simple Serializer. In your real project, this is imported from `posts.serializers`.
    """
    # Use source to access the username on the related author object
    author_username = serializers.CharField(source='author.username', read_only=True) 

    class Meta:
        model = Post 
        fields = ['id', 'author_username', 'content', 'created_at']
        read_only_fields = ['created_at']


# --- Main Feed View Implementation ---
class FeedView(ListAPIView):
    """
    Returns a personalized feed of posts from all users the current authenticated 
    user is actively following.
    
    Access: GET /api/v1/posts/feed/
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        """
        Dynamically generates the queryset by filtering posts based on the 
        current user's 'following' list.
        """
        user = self.request.user
        
        # Ensure the user object is correctly typed as the custom user model
        CustomUser = get_user_model()
        if not isinstance(user, CustomUser):
             # This should not happen if IsAuthenticated is used, but useful for robustness
             return Post.objects.none() 
        
        # 1. Efficiently retrieve the primary keys (IDs) of all users 
        # the current user is following.
        # This is enabled by the `related_name='following'` on the followers ManyToMany field.
        # The output is a flat list of integers.
        following_user_ids = user.following.values_list('id', flat=True)

        # 2. Filter the Post objects to only include those whose 'author' 
        # is in the list of followed user IDs.
        queryset = Post.objects.filter(
            author__in=following_user_ids
        ).select_related('author').order_by('-created_at') # Order by newest first

        return queryset
