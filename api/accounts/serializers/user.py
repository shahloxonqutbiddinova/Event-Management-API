from rest_framework import serializers
from ..models.user import User, DONE
from ..utils import is_mail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "phone"]


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        user = User.objects.filter(email = value).first()
        if user and user.status in ["verified", "done"]:
            raise serializers.ValidationError("Bu email allaqachon tasdiqlangan")
        return value


class CodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)

    def validate_code(self, value):
        if not value.isdigit() or len(value) != 6:
            raise serializers.ValidationError("Kod 6 ta raqamdan iborat bo'lishi kerak")
        return value


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=15)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100, required=False)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate_username(self, value):
        if User.objects.filter(username = value).exists():
            raise serializers.ValidationError("Username allaqachon band")
        return value

    def validate_phone(self, value):
        if User.objects.filter(phone = value).exists():
            raise serializers.ValidationError("Telefon raqami allaqachon ishlatilgan")
        return value

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Parollar mos emas")
        return attrs


class LoginSerializer(serializers.Serializer):
    user_input = serializers.CharField()
    password = serializers.CharField(write_only = True)

    def validate(self, attrs):
        value = attrs["user_input"]

        if is_mail(value):
            user = User.objects.filter(email = value, status = DONE).first()
            if not user:
                raise serializers.ValidationError("User topilmadi")
            attrs["username"] = user.username
        else:
            attrs["username"] = value

        return attrs
