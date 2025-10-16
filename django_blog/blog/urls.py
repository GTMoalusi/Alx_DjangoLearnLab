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

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# Set the application namespace for clarity in template usage (e.g., {% url 'blog:register' %})
app_name = 'blog'

urlpatterns = [
    # --- Custom Views ---

    # Registration page (uses our custom view)
    path('register/', views.register, name='register'),
    
    # User profile viewing page
    path('profile/', views.profile_view, name='profile_view'),

    # User profile updating/editing page
    path('profile/edit/', views.profile_update, name='profile_update'),

    # --- Django Built-in Authentication Views ---

    # Login view
    # We use Django's built-in view and point it to our custom template
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    
    # Logout view
    # We use Django's built-in view and point it to our custom template
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    
    # Optional: Password Reset Views (Highly Recommended for production apps)
    
    # 1. Start password reset (prompt for email)
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='blog/password_reset.html'), 
         name='password_reset'),
         
    # 2. Link sent confirmation page
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'), 
         name='password_reset_done'),
         
    # 3. Enter new password page (link in email)
    # The <uidb64> and <token> arguments are required by Django
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'), 
         name='password_reset_confirm'),

    # 4. Password successfully changed confirmation page
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'), 
         name='password_reset_complete'),
]
