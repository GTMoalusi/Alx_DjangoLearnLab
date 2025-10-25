from django.urls import path
from .views import NotificationListView

urlpatterns = [
    # Route for fetching the current user's notifications
    # Full path: /api/v1/notifications/
    path('', NotificationListView.as_view(), name='notification-list'),
]
