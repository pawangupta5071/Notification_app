from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    The IsOwnerOrReadOnly custom permission class is used to restrict access and modification permissions on an object based on ownership.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the owner of the notification
        return obj.user == request.user