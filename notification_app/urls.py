from django.urls import path
from .views import notification_list_get_or_create,notification_detail

urlpatterns = [
    path('notifications', notification_list_get_or_create, name='notification-list'),
    path('notifications/<int:pk>', notification_detail, name='notification-details'),
]
