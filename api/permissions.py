from rest_framework.permissions import BasePermission
from accounts.models.user import DONE


class CategoryPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return (
                request.user.is_authenticated and request.user.status == DONE
            )
        return False