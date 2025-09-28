from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import ProjectItem
from .serializers import ProjectItemSerializer

class ProjectItemListCreate(generics.ListCreateAPIView):
    """
    View for listing all ProjectItems (GET request) 
    and creating a new ProjectItem (POST request).
    
    This view uses the ProjectItemSerializer to handle data formatting and validation.
    """
    # Define the queryset (all items we can list)
    queryset = ProjectItem.objects.all()
    
    # Define the serializer class to use
    serializer_class = ProjectItemSerializer

class ProjectItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving a single ProjectItem (GET request with ID),
    updating it (PUT/PATCH requests), and deleting it (DELETE request).
    """
    # Define the queryset (all items we can look up)
    queryset = ProjectItem.objects.all()
    
    # Define the serializer class to use
    serializer_class = ProjectItemSerializer
