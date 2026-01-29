from django.db import models
from api.models.event import Event


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="tickets")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    available = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.available = self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.event.title} | {self.price} UZS"