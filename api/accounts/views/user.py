from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema

from ..serializers.user import (
    EmailSerializer, CodeSerializer,
    SignUpSerializer, LoginSerializer
)
from ..services.user_services import (
    verify_user_code, resend_verification_code, send_code_to_user
)
from ..models.user import VERIDIED, DONE
from ..utils import CustomResponse


@extend_schema(tags = ["Auth"])
class SendCodeAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = EmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = send_code_to_user(serializer.validated_data["email"])

        return CustomResponse.success(
            message="Verification code has been sent.",
            data=user.token()
        )

@extend_schema(tags = ["Auth"])
class CodeVerifyAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not verify_user_code(request.user, serializer.validated_data["code"]):
            return CustomResponse.error(
                message="Code expired or incorrect."
            )
        return CustomResponse.success(
            message="User verified successfully."
        )

@extend_schema(tags = ["Auth"])
class SignUpAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SignUpSerializer

    def post(self, request):
        user = request.user

        if user.status != VERIDIED:
            return CustomResponse.error(
                message="User has not verified email yet."
            )
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user.username = serializer.validated_data["username"]
        user.phone = serializer.validated_data["phone"]
        user.first_name = serializer.validated_data["first_name"]
        user.last_name = serializer.validated_data.get("last_name")
        user.set_password(serializer.validated_data["password"])
        user.status = DONE
        user.save()

        return CustomResponse.success(
            message="User profile completed successfully.",
            data={
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone": user.phone
            }
        )

@extend_schema(tags = ["Auth"])
class ResendCodeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if not resend_verification_code(request.user):
            return CustomResponse.error(
                message="You already have a vald code or user is verified."
            )
        return CustomResponse.success(
            message="Verification code resent successfully."
        )

@extend_schema(tags = ["Auth"])
class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request, username = serializer.validated_data["username"],
            password = serializer.validated_data["password"]
        )
        if not user:
            return CustomResponse.error(
                message="Invalid credentials."
            )
        return CustomResponse.success(
                message="User logged in successfully.",
                data = user.token()
            )
