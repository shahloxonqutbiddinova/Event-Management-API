from ..models import User, UserConfirmation, VERIDIED, NEW
from ..utils import generate_code, send_code


def send_code_to_user(email: str) -> User:
    user, _ = User.objects.get_or_create(email=email)
    code = generate_code()

    UserConfirmation.objects.create(user=user, code=code)
    send_code(email, code)

    return user


def verify_user_code(user: User, code: str) -> bool:
    confirmation = UserConfirmation.objects.filter(user=user).order_by("-created_at").first()

    if not confirmation or confirmation.is_expired():
        return False

    if confirmation.code != code:
        return False

    user.status = VERIDIED
    user.save()
    UserConfirmation.objects.filter(user=user).delete()
    return True


def resend_verification_code(user: User) -> bool:
    confirmation = UserConfirmation.objects.filter(user=user).order_by("-created_at").first()

    if not confirmation:
        return False

    if not confirmation.is_expired():
        return False

    if user.status != NEW:
        return False

    code = generate_code()
    UserConfirmation.objects.create(user=user, code=code)
    send_code(user.email, code)
    return True