from django.urls import path

from .views.user import (
    SendCodeAPIView, CodeVerifyAPIView,
    ResendCodeAPIView, SignUpAPIView, LoginAPIView,
)

app_name = "accounts"

urlpatterns = [
    path("send-code/", SendCodeAPIView.as_view(), name="send-code"),
    path("verify-code/", CodeVerifyAPIView.as_view(), name="verify-code"),
    path("resend-code/", ResendCodeAPIView.as_view(), name="resend-code"),
    path("sign-up/", SignUpAPIView.as_view(), name="sign-up"),
    path("login/", LoginAPIView.as_view(), name="login"),
]
