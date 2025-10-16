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

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile # Import the Profile model (defined in blog/models.py)

# --- 1. User Registration View ---

def register(request):
    """
    Handles user registration using the custom form.
    Automatically logs the user in upon successful registration.
    """
    if request.user.is_authenticated:
        # If the user is already logged in, redirect them away
        messages.info(request, "You are already registered and logged in.")
        return redirect('profile') # Assuming a URL name 'profile' exists

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the new user in immediately
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now logged in.')
            return redirect('profile') # Redirect to the profile page after successful registration
        else:
            # If the form is invalid, re-render it with errors
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'blog/register.html', {'form': form, 'title': 'Register'})

# --- 2. Profile Viewing View ---

@login_required
def profile_view(request):
    """
    Displays the current authenticated user's profile information.
    """
    context = {
        'title': f'{request.user.username}\'s Profile',
        'user_posts': None # Placeholder for future blog posts
    }
    return render(request, 'blog/profile_view.html', context)


# --- 3. Profile Update View ---

@login_required
def profile_update(request):
    """
    Allows the logged-in user to update their User details (username, email)
    and their custom Profile details (bio, profile picture).
    """
    if request.method == 'POST':
        # User form handles built-in User fields (username, email)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # Profile form handles custom fields (bio, profile_picture)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        
        # Validate both forms before saving anything
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been successfully updated!')
            # Use redirect to GET request to prevent 'form resubmission' warning
            return redirect('profile_update') 
        else:
            messages.error(request, "Error updating your profile. Please check the form for errors.")

    else:
        # On GET request, populate forms with current user data
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Edit Profile'
    }

    return render(request, 'blog/profile_update.html', context)
