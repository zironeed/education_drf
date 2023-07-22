from rest_framework.permissions import BasePermission
from users.models import UserRoles


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        if view.action == 'create':
            return False

        return request.user.role == UserRoles.MODERATOR


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class UserPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action == 'destroy':

            if obj.owner == request.user:
                return True

        elif view.action in ['update', 'retrieve']:

            if obj.owner == request.user:
                return True

            elif request.user.role == UserRoles.MODERATOR:
                return True

        elif view.action == 'create':

            if request.user.role == UserRoles.MODERATOR:
                return False

        else:
            return True

        raise Exception('У вас недостаточно прав')


