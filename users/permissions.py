from rest_framework import permissions


class IsStaff(permissions.BasePermission):
    """Проверка на то, что пользователь является персоналом сервиса."""

    def has_permission(self, request, view):
        return request.user.is_staff


class IsOwner(permissions.BasePermission):
    """Проверка на создателя привычки."""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
