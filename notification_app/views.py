from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import NotificationModel
from .serializers import NotificationSerializer
from rest_framework import status
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def notification_list_get_or_create(request):
    if request.method == "GET":
        notification = NotificationModel.objects.all()
        serializer = NotificationSerializer(notification, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])
def notification_detail(request,pk):
    try:
        notification = NotificationModel.objects.get(pk=pk)
    except NotificationModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = NotificationSerializer(notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

