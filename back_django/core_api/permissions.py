from rest_framework import permissions
from .models import Employee 
class IsDeveloperOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        try:       
            employee=Employee.objects.get(id=request.user.id) 
            return typeof(employee.role) == 'Developer' 
        except Employee.DoesNotExist:
            pass 
