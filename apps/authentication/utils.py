import random
from django.core.mail import send_mail
from altay_backend.config import EMAIL_HOST_USER


class Util:
    @staticmethod
    def generate_code():
        code = random.randint(100000, 999999)
        return code

    @staticmethod
    def send_verification_mail(email, code):
        subject = 'Altay verification code'
        message = f'Your verification code:\n' \
                  f'{code}\n' \
                  f'Thanks for using Altay.'
        from_email = EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, from_email, recipient_list)

    @staticmethod
    def send_reset_password_mail(email, code):
        subject = 'Altay reset password code'
        message = f'Your reset password code:\n' \
                  f'{code}\n' \
                  f'Thanks for using Altay.'
        from_email = EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, from_email, recipient_list)

