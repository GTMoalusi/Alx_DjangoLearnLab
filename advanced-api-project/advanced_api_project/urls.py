"""
URL configuration for advanced_api_project project.

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
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     # Default Django Admin path
#     path('admin/', admin.site.urls),

#     # Path that redirects all URLs starting with 'api/' to the 'api' app's urls.py
#     path('api/', include('api.urls')),
# ]

# project_tracker/urls.py
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     # Standard Django Admin interface
#     path('admin/', admin.site.urls),
    
#     # API Endpoints
#     # All URLs defined in api/urls.py will be prefixed with 'api/'
#     # This means your main endpoints are now: /api/items/ and /api/items/<id>/
#     path('api/', include('api.urls')),
    
#     # Optional: Includes the login/logout views for the browsable API
#     # This is useful for testing in your browser
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Default path for the Django Admin interface
    path('admin/', admin.site.urls),

    # MANDATORY: Include the 'api' application's URLs under the base path 'api/'
    # This directs all requests starting with '/api/' to your api/urls.py file.
    path('api/', include('api.urls')),
]
