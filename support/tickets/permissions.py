from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """Give access if user use safe methods or owner or staff"""
    def has_permission(self, request, view) -> bool:
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj) -> bool:
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.is_staff)


class OwnerOrSupportOrReadOnly(permissions.BasePermission):
    """Give access if user use safe methods or owner or support or staff"""
    def has_permission(self, request, view) -> bool:
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj) -> bool:
        return (request.method in permissions.SAFE_METHODS
                or (obj.author == request.user and request.user.is_support)
                or request.user.is_staff)


class SupportOnly(permissions.BasePermission):
    """Give access if user is support or staff"""
    def has_object_permission(self, request, view, obj) -> bool:
        return request.user.is_support or request.user.is_staff
