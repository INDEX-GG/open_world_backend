from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as admin, or is a read-only request.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsOwnerProfileOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as owner, or is a read-only request.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
