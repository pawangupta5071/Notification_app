from rest_framework import serializers
from notification_app.models import NotificationModel


class FetchNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = '__all__'