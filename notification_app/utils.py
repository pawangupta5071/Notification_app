from .models import NotificationModel
from rest_framework.response import Response
from rest_framework import status


def get_notification(pk:int) -> NotificationModel:
    try:
        notification = NotificationModel.objects.get(pk=pk)
        return notification
    except NotificationModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)