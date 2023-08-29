from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from notification_app.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from notification_app.utils import get_notification



@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])
def delete_notification(request, pk):
    if request.method == 'DELETE':
        notification = get_notification(pk)
        notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)