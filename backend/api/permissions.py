"""Creating permissions."""

from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Creating permissions of administrator."""

    def has_permission(self, request, view):
        """Enable permission of users."""
        return request.user.is_authenticated and request.user.is_admin
