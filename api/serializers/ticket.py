from rest_framework import serializers
from api.models.ticket import Ticket
from api.models.event import Event


class TicketSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.filter(is_active=True))

    class Meta:
        model = Ticket
        fields = ["id", "event", "price", "quantity", "available", "is_active", "created_at"]
        read_only_fields = ["id", "available", "created_at"]

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Ticket price must be greater than zero.")
        return value

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Ticket quantity must be greater than zero.")
        return value

    def validate(self, attrs):
        event = attrs.get("event")
        quantity = attrs.get("quantity")

        if event.status == "closed":
            raise serializers.ValidationError("Cannot create ticket for a closed event.")

        if self.instance is None:
            if Ticket.objects.filter(event=event, price=attrs.get("price")).exists():
                raise serializers.ValidationError("Ticket with this price already exists for this event.")

        if self.instance:
            sold = self.instance.quantity - self.instance.available
            if quantity is not None and quantity < sold:
                raise serializers.ValidationError(f"Quantity cannot be less than already sold tickets ({sold}).")
        return attrs
