from django.db import models
from django.conf import settings
from api.models.ticket import Ticket


User = settings.AUTH_USER_MODEL

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="bookings")
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return f"{self.user} | {self.ticket} | {self.quantity}"