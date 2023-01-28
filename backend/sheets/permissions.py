from django.conf import settings
import jwt
from rest_framework import permissions

from users.models import User


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        token = request.COOKIES.get("jwt")

        if not token:
            return False

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return False

        user = User.objects.filter(id=payload["id"]).first()

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == user
