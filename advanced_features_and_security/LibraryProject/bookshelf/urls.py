from django.urls import path
from . import views
from django.conf.urls import handler403

app_name = 'bookshelf'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'), # New URL pattern for the form
]

handler403 = 'bookshelf.views.csrf_failure'
