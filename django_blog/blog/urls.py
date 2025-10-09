from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Maps the root path of the app (which is the project root in our case) to the index view
    path('', views.index, name='home'),
]