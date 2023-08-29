from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import NotificationModel
from .serializers import CreateNotificationSerializer,FetchNotificationSerializer
from rest_framework import status
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .utils import get_notification
# Create your views here.



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_notifications(request):
    if request.method == 'GET':
        notifications = NotificationModel.objects.filter(user=request.user)
        serializer = FetchNotificationSerializer(notifications, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_notification(request):
    if request.method == 'POST':
        serializer = CreateNotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])
def view_notification(request, pk):
    if request.method == 'GET':
        notification = get_notification(pk)
        serializer = FetchNotificationSerializer(notification)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



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


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])
def delete_notification(request, pk):
    if request.method == 'DELETE':
        notification = get_notification(pk)
        notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


    

