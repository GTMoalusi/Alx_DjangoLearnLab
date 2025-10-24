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
    # 1. Django Admin Interface
    path('admin/', admin.site.urls),
    
    # 2. API Authentication (DRF login/logout for browsable API)
    # This is helpful for quick testing in the browser.
    path('api-auth/', include('rest_framework.urls')),
    
    # 3. Posts Application Endpoints (Version 1)
    # All post and comment routes will start with /api/v1/
    path('api/v1/', include('posts.urls')),
]
