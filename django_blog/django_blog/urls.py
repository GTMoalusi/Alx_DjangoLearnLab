"""
URL configuration for django_blog project.

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
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     # Admin path remains the same
#     path('admin/', admin.site.urls),
    
#     # NEW: Include the blog application's URLs.
#     # We map the root path ('') to the blog app and specify a namespace 'blog'.
#     # This allows template tags like {% url 'blog:home' %} to work.
#     path('', include('blog.urls')),
    
#     # You might also need this line if you are handling authentication (login/logout) 
#     # outside of the blog app, which is a common practice.
#     # path('accounts/', include('django.contrib.auth.urls')),
# ]

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     # Admin path remains the same
#     path('admin/', admin.site.urls),
    
#     # NEW: Include the blog application's URLs at the root path ('').
#     # Since blog.urls defines 'home', 'posts', and 'register', they are now accessible.
#     path('', include('blog.urls')),
    
#     # This path is generally needed if you plan to use Django's built-in login views
#     # path('accounts/', include('django.contrib.auth.urls')),
# ]

"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# """
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     # Admin site URL
#     path('admin/', admin.site.urls),

#     # Include all URLs from the 'blog' app.
#     # By convention, we map all blog/auth URLs to the root path '' or 'blog/'.
#     # I'll use the root path here so authentication URLs like /register and /login
#     # are easily accessible.
#     path('', include('blog.urls')),
    
#     # You might eventually want a separate path for the main blog content, 
#     # for example:
#     # path('posts/', include('blog.urls')),
# ]

"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin URL is standard
    path('admin/', admin.site.urls),
    
    # Include all URLs from the blog app at the root level
    path('', include('blog.urls')),
]
