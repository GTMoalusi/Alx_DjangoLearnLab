# from django.urls import path
# from . import views
# from .views import list_books

# urlpatterns = [
#     # Maps the URL "books/" to the list_books view
#     path('books/', views.list_books, name='list_books'),
    
#     # Maps a URL like "library/1/" to the LibraryDetailView
#     path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
# ]

# from django.urls import path, include
# from . import views
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('books/', views.list_books, name='books'),
#     path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
#     # User authentication URLs
#     path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
#     path('register/', views.register, name='register'),

#      # Role-based views
#     path('admin_page/', views.admin_view, name='admin_page'),
#     path('librarian_page/', views.librarian_view, name='librarian_page'),
#     path('member_page/', views.member_view, name='member_page'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    # Main page
    path('', views.index, name='index'),
    
    # --- URL patterns for Books with permission checks ---
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),

    # --- URL patterns for Libraries ---
    path('libraries/add/', views.add_library, name='add_library'),
]
