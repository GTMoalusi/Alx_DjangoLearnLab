from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    """
    API view to fetch a user's notifications.
    Filters by the recipient (current user) and orders by timestamp.
    All notifications fetched in the queryset are automatically marked as read.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user
        
        # 1. Fetch all notifications where the current user is the recipient
        queryset = Notification.objects.filter(recipient=user).order_by('-timestamp')
        
        return queryset

    def list(self, request, *args, **kwargs):
        """
        Overrides the list method to mark unread notifications as read 
        AFTER fetching them, and then returns the response.
        """
        # Get the queryset (which is already filtered for the current user)
        queryset = self.get_queryset()
        
        # Identify unread notifications in the current queryset
        unread_notifications = queryset.filter(is_read=False)
        
        # Mark all unread notifications in this set as read
        # Using update() is efficient as it performs the query at the database level
        unread_notifications.update(is_read=True)
        
        # Proceed with standard serialization and response generation
        serializer = self.get_serializer(queryset, many=True)
        return generics.Response(serializer.data)
