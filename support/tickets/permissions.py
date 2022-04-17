from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.is_staff)


class OwnerOrSupportOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or (obj.author == request.user and request.user.is_support)
                or request.user.is_staff)


class SupportOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_support or request.user.is_staff
