from rest_framework import serializers
from api.models.booking import Booking
from api.models.ticket import Ticket
from api.models import DONE


class BookingSerializer(serializers.ModelSerializer):
    ticket = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.filter(is_active=True))

    class Meta:
        model = Booking
        fields = ["id", "ticket", "quantity", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Booking quantity must be greater than zero.")
        return value

    def validate(self, attrs):
        request = self.context.get("request")
        ticket = attrs.get("ticket")
        quantity = attrs.get("quantity")

        if request.user.status != DONE:
            raise serializers.ValidationError(
                "Only verified users can make bookings."
            )
        if ticket.available < quantity:
            raise serializers.ValidationError(
                "Not enough tickets available."
            )
        return attrs

    def create(self, validated_data):
        request = self.context.get("request")
        ticket = validated_data["ticket"]
        quantity = validated_data["quantity"]
        ticket.available -= quantity
        ticket.save(update_fields=["available"])

        return Booking.objects.create(user=request.user, ticket=ticket, quantity=quantity,)
