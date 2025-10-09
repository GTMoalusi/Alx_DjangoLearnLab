from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User # Required to create dummy posts

def index(request):
    """
    Displays the list of all blog posts on the home page.
    """
    # Fetch all published posts
    posts = Post.objects.all()
    
    # --- For initial testing purposes only: Create a dummy post if none exists ---
    if not posts.exists():
        try:
            # Find the first user or create a temporary one
            user = User.objects.first()
            if not user:
                user = User.objects.create_user(username='admin', email='a@example.com', password='password')
                user.is_superuser = True
                user.is_staff = True
                user.save()
            
            Post.objects.create(
                title="Welcome to Django Blog!",
                content="This is your first blog post. Your setup is working! Find this template in blog/templates/blog/index.html.",
                author=user
            )
            posts = Post.objects.all() # Refetch with new post
        except Exception:
            # Handle cases where the database might not be migrated yet
            pass
    # ----------------------------------------------------------------------------
    
    context = {'posts': posts}
    return render(request, 'blog/base.html', context)
