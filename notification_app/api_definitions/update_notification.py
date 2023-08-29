from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from notification_app.defined_serializers import CreateNotificationSerializer
from rest_framework import status
from notification_app.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from notification_app.utils import get_notification


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])
def update_notification(request, pk):
    if request.method == 'PUT':
        notification = get_notification(pk)
        serializer = CreateNotificationSerializer(notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)