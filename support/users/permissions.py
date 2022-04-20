from xmlrpc.client import Boolean
from rest_framework import permissions


class MePermission(permissions.BasePermission):
    """Give access if user is authenticated or staff"""
    def has_permission(self, request, view) -> Boolean:
        return (
            request.user
            and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj) -> Boolean:
        return (
            request.is_staff
            or obj == request.user
        )
