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

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
# Import the form we defined in blog/forms.py
from .forms import CustomUserCreationForm 

# View function for the Home page, linked to name='home'
def index(request):
    """
    Renders the home page of the blog.
    """
    return render(request, 'blog/base.html', {
        "welcome_message": "Welcome to the Django Blog Home Page!"
    })

# The view function for the Blog Posts page, linked to name='posts'
def posts(request):
    """
    Renders the main list of all blog posts.
    """
    return render(request, 'blog/base.html', {
        "page_title": "All Blog Posts",
        "content_message": "This is where all the blog posts will be listed."
    })

# NEW: Registration view, mapped to name='register'
def register(request):
    """
    Handles user registration using the CustomUserCreationForm.
    If the form is valid, it saves the user, logs them in, and redirects to the home page.
    """
    if request.method == 'POST':
        # If the request is POST, process the submitted form data
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user object
            user = form.save()
            
            # Log the newly created user in immediately
            login(request, user)
            
            # Redirect to the home page after successful registration
            return redirect(reverse('home'))
    else:
        # If the request is GET, show a blank form
        form = CustomUserCreationForm()
    
    # Render the registration form template, passing the form object
    return render(request, 'blog/register.html', {'form': form})
