# from django.shortcuts import render
# from .models import Post
# from django.contrib.auth.models import User # Required to create dummy posts

# def index(request):
#     """
#     Displays the list of all blog posts on the home page.
#     """
#     # Fetch all published posts
#     posts = Post.objects.all()
    
#     # --- For initial testing purposes only: Create a dummy post if none exists ---
#     if not posts.exists():
#         try:
#             # Find the first user or create a temporary one
#             user = User.objects.first()
#             if not user:
#                 user = User.objects.create_user(username='admin', email='a@example.com', password='password')
#                 user.is_superuser = True
#                 user.is_staff = True
#                 user.save()
            
#             Post.objects.create(
#                 title="Welcome to Django Blog!",
#                 content="This is your first blog post. Your setup is working! Find this template in blog/templates/blog/index.html.",
#                 author=user
#             )
#             posts = Post.objects.all() # Refetch with new post
#         except Exception:
#             # Handle cases where the database might not be migrated yet
#             pass
#     # ----------------------------------------------------------------------------
    
#     context = {'posts': posts}
#     return render(request, 'blog/base.html', context)

# from django.shortcuts import render

# # View function for the Home page, linked to name='home'
# def index(request):
#     """
#     Renders the home page of the blog.
#     Currently renders the base template as a placeholder.
#     """
#     return render(request, 'blog/base.html', {
#         "welcome_message": "Welcome to the Django Blog Home Page!"
#     })

# # The missing view function for the Blog Posts page, linked to name='posts'
# def posts(request):
#     """
#     Renders the main list of all blog posts.
#     """
#     return render(request, 'blog/base.html', {
#         "page_title": "All Blog Posts",
#         "content_message": "This is where all the blog posts will be listed."
#     })

# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from django.urls import reverse
# # Import the form we defined in blog/forms.py
# from .forms import CustomUserCreationForm 

# # View function for the Home page, linked to name='home'
# def index(request):
#     """
#     Renders the home page of the blog.
#     """
#     return render(request, 'blog/base.html', {
#         "welcome_message": "Welcome to the Django Blog Home Page!"
#     })

# # The view function for the Blog Posts page, linked to name='posts'
# def posts(request):
#     """
#     Renders the main list of all blog posts.
#     """
#     return render(request, 'blog/base.html', {
#         "page_title": "All Blog Posts",
#         "content_message": "This is where all the blog posts will be listed."
#     })

# # NEW: Registration view, mapped to name='register'
# def register(request):
#     """
#     Handles user registration using the CustomUserCreationForm.
#     If the form is valid, it saves the user, logs them in, and redirects to the home page.
#     """
#     if request.method == 'POST':
#         # If the request is POST, process the submitted form data
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             # Save the new user object
#             user = form.save()
            
#             # Log the newly created user in immediately
#             login(request, user)
            
#             # Redirect to the home page after successful registration
#             return redirect(reverse('home'))
#     else:
#         # If the request is GET, show a blank form
#         form = CustomUserCreationForm()
    
#     # Render the registration form template, passing the form object
#     return render(request, 'blog/register.html', {'form': form})

# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm
# from .models import Profile # Import the Profile model (defined in blog/models.py)

# # --- 1. User Registration View ---

# def register(request):
#     """
#     Handles user registration using the custom form.
#     Automatically logs the user in upon successful registration.
#     """
#     if request.user.is_authenticated:
#         # If the user is already logged in, redirect them away
#         messages.info(request, "You are already registered and logged in.")
#         return redirect('profile') # Assuming a URL name 'profile' exists

#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Log the new user in immediately
#             login(request, user)
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}! You are now logged in.')
#             return redirect('profile') # Redirect to the profile page after successful registration
#         else:
#             # If the form is invalid, re-render it with errors
#             messages.error(request, "Registration failed. Please correct the errors below.")
#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'blog/register.html', {'form': form, 'title': 'Register'})

# # --- 2. Profile Viewing View ---

# @login_required
# def profile_view(request):
#     """
#     Displays the current authenticated user's profile information.
#     """
#     context = {
#         'title': f'{request.user.username}\'s Profile',
#         'user_posts': None # Placeholder for future blog posts
#     }
#     return render(request, 'blog/profile_view.html', context)


# # --- 3. Profile Update View ---

# @login_required
# def profile_update(request):
#     """
#     Allows the logged-in user to update their User details (username, email)
#     and their custom Profile details (bio, profile picture).
#     """
#     if request.method == 'POST':
#         # User form handles built-in User fields (username, email)
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         # Profile form handles custom fields (bio, profile_picture)
#         p_form = ProfileUpdateForm(request.POST, 
#                                    request.FILES, 
#                                    instance=request.user.profile)
        
#         # Validate both forms before saving anything
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, 'Your account has been successfully updated!')
#             # Use redirect to GET request to prevent 'form resubmission' warning
#             return redirect('profile_update') 
#         else:
#             messages.error(request, "Error updating your profile. Please check the form for errors.")

#     else:
#         # On GET request, populate forms with current user data
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#         'title': 'Edit Profile'
#     }

# #     return render(request, 'blog/profile_update.html', context)
# from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy, reverse
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# from .models import Post, Comment
# from .forms import CommentForm # Make sure CommentForm is imported

# # =======================================================================
# # POST CRUD Views (Simplified placeholders - assuming these exist)
# # =======================================================================

# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/post_list.html'
#     context_object_name = 'posts'

# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'content'] # Adjusted fields based on common implementation
    
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     fields = ['title', 'content']
    
#     def test_func(self):
#         post = self.get_object()
#         return post.author == self.request.user

# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Post
#     success_url = reverse_lazy('blog:post_list')
    
#     def test_func(self):
#         post = self.get_object()
#         return post.author == self.request.user

# # =======================================================================
# # POST Detail View (Modified to handle Comment Creation)
# # =======================================================================

# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'
#     context_object_name = 'post'

#     def get_context_data(self, **kwargs):
#         """Adds the blank CommentForm to the context for display."""
#         context = super().get_context_data(**kwargs)
#         # Add the CommentForm to the context for display in the template
#         context['form'] = CommentForm() 
#         return context

#     def post(self, request, *args, **kwargs):
#         """Handles the submission of the CommentForm."""
#         self.object = self.get_object() # Get the specific Post object

#         # 1. Check if the user is authenticated (required for posting comments)
#         if not request.user.is_authenticated:
#             # Redirect to login, passing the current page URL for 'next'
#             return redirect(f"{reverse_lazy('login')}?next={self.object.get_absolute_url()}")

#         # 2. Process the form data
#         form = CommentForm(request.POST)
        
#         if form.is_valid():
#             # Create a new Comment object but don't save to database yet (commit=False)
#             comment = form.save(commit=False)
            
#             # Set the foreign keys which are not in the form
#             comment.post = self.object
#             comment.author = request.user
            
#             # Save the new comment to the database
#             comment.save()
            
#             # Redirect to the same post detail page after successful comment
#             return redirect(self.object.get_absolute_url())
        
#         # 3. If the form is invalid, re-render the detail page with errors
#         context = self.get_context_data(object=self.object)
#         context['form'] = form # Pass the form back with errors
#         return self.render_to_response(context)


# # =======================================================================
# # COMMENT CRUD Views (Requires Login and Permission Checks)
# # =======================================================================

# class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = 'blog/comment_form.html' # Reusing the form template for updates
#     context_object_name = 'comment'

#     def get_success_url(self):
#         """Redirects to the post detail page after successful update."""
#         return self.object.post.get_absolute_url()

#     def test_func(self):
#         """Ensures only the comment author can update it."""
#         comment = self.get_object()
#         return comment.author == self.request.user


# class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Comment
#     template_name = 'blog/comment_confirm_delete.html'
#     context_object_name = 'comment'

#     def get_success_url(self):
#         """Redirects to the post detail page after successful deletion."""
#         # Note: self.object.post is still accessible here even after deletion confirmation
#         return self.object.post.get_absolute_url()

#     def test_func(self):
#         """Ensures only the comment author can delete it."""
#         comment = self.get_object()
#         return comment.author == self.request.user

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

# Import models and forms
from .models import Post, Comment
from .forms import PostForm, CommentForm

# --- Mixins for Permission Checks ---

class AuthorRequiredMixin(UserPassesTestMixin):
    """
    Mixin to check if the current user is the author of the object.
    Used for Post and Comment Update/Delete views.
    """
    def test_func(self):
        # Retrieve the object being operated on (Post or Comment)
        obj = self.get_object()
        # Ensure the object's author matches the request user
        return obj.author == self.request.user

# --- Post Views (Existing/Referenced) ---

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    """
    Displays a single Post and handles the creation of a new Comment via POST.
    """
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    # Inject the CommentForm into the context for rendering on the detail page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # We always provide a fresh CommentForm
        context['comment_form'] = CommentForm()
        return context

    # Handle POST requests to create a new comment
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Initialize the form with data from the request
        comment_form = CommentForm(request.POST)

        # 1. Check if the form is valid and the user is logged in
        if comment_form.is_valid() and request.user.is_authenticated:
            # Create the comment instance but don't save to the database yet (commit=False)
            new_comment = comment_form.save(commit=False)
            
            # Manually set the Foreign Key fields
            new_comment.post = self.object # Link to the current post
            new_comment.author = request.user # Link to the logged-in user
            
            # Save the fully populated instance
            new_comment.save()
            
            # Redirect back to the post detail page
            return redirect(self.object.get_absolute_url()) 
        else:
            # If form is invalid or user is not logged in, re-render the page
            # Re-fetch context data (including the post)
            context = self.get_context_data()
            # Pass the invalid form back to show any errors
            context['comment_form'] = comment_form 
            return self.render_to_response(context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'slug': self.object.slug})

class PostDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:posts')

# --- NEW Comment Views ---

class CommentUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    """
    Allows the author to edit their existing comment.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    context_object_name = 'comment'

    def get_success_url(self):
        # Redirect back to the post detail page after successful update
        return reverse_lazy('blog:post_detail', kwargs={'slug': self.object.post.slug})

class CommentDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    """
    Allows the author to delete their comment.
    """
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    context_object_name = 'comment'

    def get_success_url(self):
        # Redirect back to the post detail page after successful deletion
        return reverse_lazy('blog:post_detail', kwargs={'slug': self.object.post.slug})

# --- Other Views (e.g., register) ---

@login_required
def home_view(request):
    return render(request, 'blog/home.html')
