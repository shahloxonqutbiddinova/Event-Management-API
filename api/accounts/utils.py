from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

import random
import string
import re


def send_code(email: str, code: str):
    text = f"Event Management tizimi uchun tastiqlash kodingiz: {code}"
    send_mail(
        subject = "Verification Code",
        from_email = settings.DEFAULT_FROM_EMAIL,
        message = text,
        recipient_list = [email],
        fail_silently = False
    )


def generate_code(size = 6, chars = string.digits):
    return "".join(random.choice(chars) for _ in range(size))


class CustomResponse:
    @staticmethod
    def success(message, data = None):
        return Response(
            {
                "status": True,
                "message": message,
                "data": data
            },
            status = status.HTTP_200_OK
        )

    @staticmethod
    def error(message, data = None):
        return Response(
            {
                "status": False,
                "message": message,
                "data": data
            },
            status = status.HTTP_400_BAD_REQUEST
        )

def is_mail(email: str):
    return re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
