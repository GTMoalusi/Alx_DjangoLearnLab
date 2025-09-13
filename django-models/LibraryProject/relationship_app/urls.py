# from django.urls import path
# from . import views
# from .views import list_books

# urlpatterns = [
#     # Maps the URL "books/" to the list_books view
#     path('books/', views.list_books, name='list_books'),
    
#     # Maps a URL like "library/1/" to the LibraryDetailView
#     path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
# ]

from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', views.list_books, name='books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # User authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]