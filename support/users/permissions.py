from rest_framework import permissions


class MePermission(permissions.BasePermission):
    """Give access if user is authenticated or staff"""
    def has_permission(self, request, view) -> bool:
        return (
            request.user
            and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj) -> bool:
        return (
            request.is_staff
            or obj == request.user
        )
