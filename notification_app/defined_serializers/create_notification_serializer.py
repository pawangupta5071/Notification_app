from rest_framework import serializers
from notification_app.models import NotificationModel

class CreateNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = ['message']