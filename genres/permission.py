from rest_framework import permissions

class GenresPermissionClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return True