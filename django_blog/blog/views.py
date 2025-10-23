from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q # Used for complex lookups (OR conditions)

# Import Models and Forms
from .models import Post, Comment
from .forms import PostForm, CommentForm


# --- Mixins (Common functions for class-based views) ---

class AuthorRequiredMixin(UserPassesTestMixin):
    """
    Mixin to ensure only the author of the POST can edit/delete it.
    """
    def test_func(self):
        # Retrieve the object (Post instance) that the view is operating on
        obj = self.get_object()
        # Check if the current user is the author of the post
        return obj.author == self.request.user

class CommentAuthorRequiredMixin(UserPassesTestMixin):
    """
    Mixin to ensure only the author of the COMMENT can edit/delete it.
    """
    def test_func(self):
        # Retrieve the object (Comment instance) that the view is operating on
        obj = self.get_object()
        # Check if the current user is the author of the comment
        return obj.author == self.request.user


# --- Post Views ---


class PostSearchView(ListView):
    """
    Handles displaying search results for blog posts.
    Allows searching across title, content, and tags.
    """
    model = Post
    template_name = 'blog/post_search.html' # Don't forget to create this template!
    context_object_name = 'posts'
    paginate_by = 10 # Optional: Add pagination for results

    def get_queryset(self):
        # Start with all Post objects
        queryset = Post.objects.all()
        
        # Get the search query from the URL parameters (e.g., /search/?q=term)
        query = self.request.GET.get('q')

        if query:
            # Use Q objects to perform an OR query across multiple fields
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct() # Use distinct() to prevent duplicate posts if they match multiple tags

        return queryset


class PostListView(ListView):
    """
    Displays a list of all published blog posts.
    """
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    # Order posts by creation date, newest first
    ordering = ['-date_created']
    # 5 posts per page
    paginate_by = 5 


class PostDetailView(DetailView):
    """
    Displays a single blog post and its associated comments.
    """
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        """
        Adds CommentForm and existing comments to the context.
        """
        context = super().get_context_data(**kwargs)
        # Add the CommentForm for users to submit new comments
        context['comment_form'] = CommentForm() 
        # Fetch approved comments, ordered newest first
        context['comments'] = self.object.comments.filter(approved=True).order_by('-date_created') 
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new post. Requires user to be logged in.
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        # Automatically set the author of the post to the currently logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    """
    View for updating an existing post. Requires user to be logged in and to be the author.
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    

class PostDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    """
    View for deleting an existing post. Requires user to be logged in and to be the author.
    """
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    # Redirect to the homepage after successful deletion
    success_url = reverse_lazy('blog:post_list')


# --- Comment Views ---

class CommentCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new comment on a specific post.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post_detail.html'

    def form_valid(self, form):
        # Get the parent post from the URL (pk is passed in the URL for the Post)
        # Assuming the URL uses the post's slug
        post = get_object_or_404(Post, slug=self.kwargs.get('slug')) 
        
        # Set the comment's author and parent post
        form.instance.author = self.request.user
        form.instance.post = post
        
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the post detail page after submitting a comment.
        return reverse('blog:post_detail', kwargs={'slug': self.object.post.slug})


class CommentUpdateView(LoginRequiredMixin, CommentAuthorRequiredMixin, UpdateView):
    """
    View for updating an existing comment.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_success_url(self):
        # Redirect back to the post detail page after updating a comment.
        return reverse('blog:post_detail', kwargs={'slug': self.object.post.slug})


class CommentDeleteView(LoginRequiredMixin, CommentAuthorRequiredMixin, DeleteView):
    """
    View for deleting an existing comment.
    """
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        # Redirect back to the post detail page after deleting a comment.
        return reverse('blog:post_detail', kwargs={'slug': self.object.post.slug})
