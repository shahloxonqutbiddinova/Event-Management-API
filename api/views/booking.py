from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api.models.booking import Booking
from api.serializers.booking import BookingSerializer
from api.permissions import BookingPermission


class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, BookingPermission]

    def get_queryset(self):
        return (Booking.objects.select_related("ticket", "ticket__event").filter(user=self.request.user))

    def perform_create(self, serializer):
        serializer.save()
