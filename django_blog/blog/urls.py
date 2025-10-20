# from django.urls import path
# from . import views

# # Set app_name to allow for namespacing (e.g., blog:home)
# app_name = "blog"

# urlpatterns = [
#     # ex: /
#     path("", views.index, name="home"),
#     # ex: /posts/
#     path("posts/", views.posts, name="posts"),
    
#     # NEW: ex: /register/ - This path defines the 'register' name.
#     path("register/", views.register, name="register"), 
# ]

# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views

# # Set the application namespace for clarity in template usage (e.g., {% url 'blog:register' %})
# app_name = 'blog'

# urlpatterns = [
#     # --- Custom Views ---

#     # Registration page (uses our custom view)
#     path('register/', views.register, name='register'),
    
#     # User profile viewing page
#     path('profile/', views.profile_view, name='profile_view'),

#     # User profile updating/editing page
#     path('profile/edit/', views.profile_update, name='profile_update'),

#     # --- Django Built-in Authentication Views ---

#     # Login view
#     # We use Django's built-in view and point it to our custom template
#     path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    
#     # Logout view
#     # We use Django's built-in view and point it to our custom template
#     path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    
#     # Optional: Password Reset Views (Highly Recommended for production apps)
    
#     # 1. Start password reset (prompt for email)
#     path('password-reset/', 
#          auth_views.PasswordResetView.as_view(template_name='blog/password_reset.html'), 
#          name='password_reset'),
         
#     # 2. Link sent confirmation page
#     path('password-reset/done/', 
#          auth_views.PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'), 
#          name='password_reset_done'),
         
#     # 3. Enter new password page (link in email)
#     # The <uidb64> and <token> arguments are required by Django
#     path('password-reset-confirm/<uidb64>/<token>/', 
#          auth_views.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'), 
#          name='password_reset_confirm'),

#     # 4. Password successfully changed confirmation page
#     path('password-reset-complete/', 
#          auth_views.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'), 
#          name='password_reset_complete'),
# ]

# from django.urls import path
# from . import views
# from .views import (
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView
# )

# # Mandatory for namespacing
# app_name = 'blog'

# urlpatterns = [
#     # Home/Index page (using the function-based view from blog/views.py)
#     path('home/', views.index, name='index'),

#     # READ: List all posts
#     # URL: /blog/
#     path('', PostListView.as_view(), name='post_list'),

#     # READ: Detail view for a single post
#     # URL: /blog/post/12/
#     path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

#     # CREATE: View to create a new post
#     # URL: /blog/post/new/
#     path('post/new/', PostCreateView.as_view(), name='post_create'),

#     # UPDATE: View to edit an existing post (requires primary key)
#     # URL: /blog/post/12/edit/
#     path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),

#     # DELETE: View to delete an existing post (requires primary key)
#     # URL: /blog/post/12/delete/
#     path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
# ]

# from django.urls import path
# from . import views

# app_name = 'blog'

# urlpatterns = [
#     # READ: Post List View (All posts)
#     path('', views.PostListView.as_view(), name='post_list'),
    
#     # READ: Post Detail View (Single post)
#     path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    
#     # CREATE: Create Post View
#     path('post/new/', views.PostCreateView.as_view(), name='post_create'),

#     # UPDATE: Edit Post View (Corrected to use '/update/')
#     # This URL pattern is now: post/<int:pk>/update/
#     path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    
#     # DELETE: Delete Post View
#     path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
# ]

# from django.urls import path
# from .views import (
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView,
#     CommentUpdateView,  # Import the new views
#     CommentDeleteView,  # Import the new views
# )

# # Define the application namespace
# app_name = 'blog'

# urlpatterns = [
#     # Post URLs
#     path('', PostListView.as_view(), name='post_list'),
#     path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
#     path('new/', PostCreateView.as_view(), name='post_create'),
#     path('<slug:slug>/edit/', PostUpdateView.as_view(), name='post_update'),
#     path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
#     # Comment URLs
#     # We use <int:pk> here because the primary key refers to the Comment model itself
#     path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
#     path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
# ]

# from django.urls import path
# from . import views
# from .views import (
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView,
#     CommentUpdateView, # Necessary to define URL path
#     CommentDeleteView, # Necessary to define URL path
# )

# app_name = "blog"

# urlpatterns = [
#     # General View
#     path('', views.home_view, name='home'),

#     # --- Post Views ---
#     # List of all posts
#     path('posts/', PostListView.as_view(), name='posts'),
#     # Create a new post
#     path('posts/new/', PostCreateView.as_view(), name='post_create'),
#     # Detail view (also handles Comment Creation via POST)
#     path('posts/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
#     # Update an existing post
#     path('posts/<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
#     # Delete an existing post
#     path('posts/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),

#     # --- Comment Views ---
#     # Update an existing comment (using the comment's primary key)
#     path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
#     # Delete an existing comment (using the comment's primary key)
#     path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
# ]

# from django.shortcuts import render, get_object_or_404
# from django.views.generic import (
#     ListView, 
#     DetailView, 
#     CreateView, 
#     UpdateView, 
#     DeleteView
# )
# from django.urls import reverse_lazy, reverse
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from .models import Post, Comment
# from .forms import PostForm, CommentForm


# # --- Mixins (Common functions for class-based views) ---

# class AuthorRequiredMixin(UserPassesTestMixin):
#     """
#     Mixin to ensure only the author of the POST can edit/delete it.
#     """
#     def test_func(self):
#         # Retrieve the object (Post instance) that the view is operating on
#         obj = self.get_object()
#         # Check if the current user is the author of the post
#         return obj.author == self.request.user

# class CommentAuthorRequiredMixin(UserPassesTestMixin):
#     """
#     Mixin to ensure only the author of the COMMENT can edit/delete it.
#     """
#     def test_func(self):
#         # Retrieve the object (Comment instance) that the view is operating on
#         obj = self.get_object()
#         # Check if the current user is the author of the comment
#         return obj.author == self.request.user


# # --- Post Views ---

# class PostListView(ListView):
#     """
#     Displays a list of all published blog posts.
#     """
#     model = Post
#     template_name = 'blog/post_list.html'
#     context_object_name = 'posts'
#     # Order posts by creation date, newest first
#     ordering = ['-date_created']
#     # 5 posts per page
#     paginate_by = 5 


# class PostDetailView(DetailView):
#     """
#     Displays a single blog post and its associated comments.
#     """
#     model = Post
#     template_name = 'blog/post_detail.html'
#     context_object_name = 'post'

#     def get_context_data(self, **kwargs):
#         """
#         Adds CommentForm and existing comments to the context.
#         """
#         context = super().get_context_data(**kwargs)
#         # Add the CommentForm for users to submit new comments
#         context['comment_form'] = CommentForm() 
#         # Fetch approved comments, ordered newest first
#         context['comments'] = self.object.comments.filter(approved=True).order_by('-date_created') 
#         return context


# class PostCreateView(LoginRequiredMixin, CreateView):
#     """
#     View for creating a new post. Requires user to be logged in.
#     """
#     model = Post
#     form_class = PostForm
#     template_name = 'blog/post_form.html'
    
#     def form_valid(self, form):
#         # Automatically set the author of the post to the currently logged-in user
#         form.instance.author = self.request.user
#         return super().form_valid(form)


# class PostUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
#     """
#     View for updating an existing post. Requires user to be logged in and to be the author.
#     """
#     model = Post
#     form_class = PostForm
#     template_name = 'blog/post_form.html'
    

# class PostDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
#     """
#     View for deleting an existing post. Requires user to be logged in and to be the author.
#     """
#     model = Post
#     template_name = 'blog/post_confirm_delete.html'
#     # Redirect to the homepage after successful deletion
#     success_url = reverse_lazy('blog:post_list')


# # --- Comment Views ---

# class CommentCreateView(LoginRequiredMixin, CreateView):
#     """
#     View for creating a new comment on a specific post. Requires user to be logged in.
#     The post's primary key (pk) must be passed in the URL.
#     """
#     model = Comment
#     form_class = CommentForm
#     template_name = 'blog/post_detail.html' # Use the detail template for display, but form submits here

#     def form_valid(self, form):
#         # Get the parent post from the URL (pk is passed in the URL for the Post)
#         post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        
#         # Set the comment's author and parent post
#         form.instance.author = self.request.user
#         form.instance.post = post
        
#         return super().form_valid(form)

#     def get_success_url(self):
#         # Redirect back to the post detail page after submitting a comment.
#         return reverse('blog:post_detail', kwargs={'pk': self.object.post.pk, 'slug': self.object.post.slug})


# class CommentUpdateView(LoginRequiredMixin, CommentAuthorRequiredMixin, UpdateView):
#     """
#     View for updating an existing comment. Requires user to be logged in and be the comment author.
#     """
#     model = Comment
#     form_class = CommentForm
#     template_name = 'blog/comment_form.html' # You will need to create this template later

#     def get_success_url(self):
#         # Redirect back to the post detail page after updating a comment.
#         return reverse('blog:post_detail', kwargs={'pk': self.object.post.pk, 'slug': self.object.post.slug})


# class CommentDeleteView(LoginRequiredMixin, CommentAuthorRequiredMixin, DeleteView):
#     """
#     View for deleting an existing comment. Requires user to be logged in and be the comment author.
#     """
#     model = Comment
#     template_name = 'blog/comment_confirm_delete.html' # You will need to create this template later

#     def get_success_url(self):
#         # Redirect back to the post detail page after deleting a comment.
#         return reverse('blog:post_detail', kwargs={'pk': self.object.post.pk, 'slug': self.object.post.slug})

from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

# This defines the namespace for your app, used for reverse lookups like 'blog:post_list'
app_name = 'blog'

urlpatterns = [
    # --- Post URLs (CRUD) ---
    # Home/List View: /
    path('', PostListView.as_view(), name='post_list'),

    # Detail View: /<post_pk>/<post_slug>/
    path('<int:pk>/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),

    # Create View: /new/
    path('new/', PostCreateView.as_view(), name='post_create'),

    # Update View: /<post_pk>/<post_slug>/update/
    path('<int:pk>/<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),

    # Delete View: /<post_pk>/<post_slug>/delete/
    path('<int:pk>/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),


    # --- Comment URLs (CRUD) ---
    # Create View (uses the POST's PK): /<post_pk>/comment/create/
    path('<int:pk>/comment/create/', CommentCreateView.as_view(), name='comment_create'),

    # Update View (uses the COMMENT's PK): /comment/<comment_pk>/update/
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),

    # Delete View (uses the COMMENT's PK): /comment/<comment_pk>/delete/
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
