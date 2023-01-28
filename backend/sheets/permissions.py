from rest_framework import permissions

from sheets.services import get_current_user


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        user = get_current_user(request)

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == user


class IsAuthenticatedCustom(permissions.BasePermission):
    """
    Custom permission to only authenticated people.
    """

    def has_permission(self, request, view):
        user = get_current_user(request)
        return True if user else False
