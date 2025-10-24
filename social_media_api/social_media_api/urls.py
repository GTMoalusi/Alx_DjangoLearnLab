"""
URL configuration for social_media_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# social_media_api/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin Site
    path('admin/', admin.site.urls),
    
    # New: Include URLs for the 'accounts' application (e.g., /api/v1/accounts/login, etc.)
    path('accounts/', include('accounts.urls')),
    
    # Include URLs for the 'posts' application (assuming this handles posts)
    # You might prefix this with 'api/v1/' depending on your structure
    path('api/v1/posts/', include('posts.urls')),
    
    # You can add other app URLs here as needed
]