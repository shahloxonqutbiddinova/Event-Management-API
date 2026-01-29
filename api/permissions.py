from rest_framework.permissions import BasePermission
from api.models import DONE
from api.models.ticket import Ticket


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
        return obj.owner == request.user


class TicketPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH", "DELETE"]:
            return obj.event.owner == request.user
        return True

class BookingPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method == "POST":
            return request.user.status == DONE
        return True

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user