from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from notification_app.defined_serializers import FetchNotificationSerializer
from rest_framework import status
from notification_app.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from notification_app.utils import get_notification


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])
def view_notification(request, pk):
    if request.method == 'GET':
        notification = get_notification(pk)
        serializer = FetchNotificationSerializer(notification)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)