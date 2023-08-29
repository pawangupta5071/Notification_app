from rest_framework.decorators import api_view, permission_classes
from notification_app.models import NotificationModel
from rest_framework.response import Response
from notification_app.defined_serializers import FetchNotificationSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_notifications(request):
    if request.method == 'GET':
        notifications = NotificationModel.objects.filter(user=request.user)
        serializer = FetchNotificationSerializer(notifications, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)