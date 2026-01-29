from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, ValidationError

from api.models.ticket import Ticket
from api.serializers.ticket import TicketSerializer
from api.permissions import TicketPermission


class TicketViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, TicketPermission]
    queryset = Ticket.objects.select_related("event", "event__owner").filter(is_active=True)

    def get_queryset(self):
        queryset = super().get_queryset()
        event_id = self.request.query_params.get("event")

        if event_id:
            queryset = queryset.filter(event_id=event_id)
        return queryset

    def perform_create(self, serializer):
        event = serializer.validated_data["event"]
        if event.owner != self.request.user:
            raise PermissionDenied("Only event owner can create tickets.")

        price = serializer.validated_data["price"]
        if Ticket.objects.filter(event=event, price=price).exists():
            raise ValidationError(
                "Ticket with this price already exists for this event."
            )
        serializer.save()

    def perform_update(self, serializer):
        instance = self.get_object()

        new_quantity = serializer.validated_data.get("quantity")
        if new_quantity is not None:
            sold = instance.quantity - instance.available
            if new_quantity < sold:
                raise ValidationError(f"Quantity cannot be less than sold tickets ({sold}).")

        serializer.save()