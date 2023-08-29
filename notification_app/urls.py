from django.urls import path
from .views import fetch_notifications,create_notification,view_notification,delete_notification,update_notification

urlpatterns = [
    path('create_notifications', create_notification, name='create_notification'),
    path('fetch_notifications', fetch_notifications, name='fetch_notification'),
    path('view_notifications/<int:pk>', view_notification, name='view_notification'),
    path('update_notifications/<int:pk>', update_notification, name='update_notification'),
    path('delete_notifications/<int:pk>', delete_notification, name='delete_notification'),
]