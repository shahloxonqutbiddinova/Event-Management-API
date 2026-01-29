from django.db import models
from django.conf import settings
from django.utils.text import slugify

from api.models.category import Category


class Event(models.Model):
    STATUS_CHOICES = (
        ("new", "New"),
        ("active", "Active"),
        ("closed", "Closed"),
    )

    ower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="events")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="events")
    title = models.CharField(max_length=260)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    description = models.TextField()
    location = models.CharField(max_length=260)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-start_time"]
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["start_time"]),
        ]

    def save( self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.ower})"
