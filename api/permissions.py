from rest_framework.permissions import BasePermission
from api.accounts.models.user import DONE


class CategoryPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return (
                request.user.is_authenticated and request.user.status == DONE
            )
        return False

class EventPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        if request.method == "POST":
            return (request.user.is_authenticated and request.user.status == DONE)
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        return obj.ower == request.user