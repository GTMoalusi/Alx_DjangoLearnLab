from django.urls import path
from . import views

# Set app_name to allow for namespacing (e.g., blog:home)
app_name = "blog"

urlpatterns = [
    # ex: /
    path("", views.index, name="home"),
    # ex: /posts/
    path("posts/", views.posts, name="posts"),
    
    # NEW: ex: /register/ - This path defines the 'register' name.
    path("register/", views.register, name="register"), 
]
