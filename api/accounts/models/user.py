from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
import uuid


NEW, VERIDIED, DONE = ("new", "veridied", "done")

STATUS_CHOICES = (
    (NEW, "NEW"),
    (VERIDIED, "VERIFIED"),
    (DONE, "DONE"),
)


class User(AbstractUser):
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=NEW)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="users/", null=True, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = f"user-{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)

    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }



class UserConfirmation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="confirmations")
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.expired_at = timezone.now() + timezone.timedelta(minutes=2)
        super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() > self.expired_at

    def __str__(self):
        return f"{self.user.username} | {self.code}"