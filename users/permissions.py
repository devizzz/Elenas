"""User permission classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from users.models import User


class HasPermission(BasePermission):
    """Allow access to create experience, extras and proyects."""

    def has_permission(self, request, view):

        try:
            user = User.objects.get(
                email=request.user
            )
        except User.DoesNotExist:
            return False
        return True