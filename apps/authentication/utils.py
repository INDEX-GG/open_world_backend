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
        subject = 'Код для регистрации'
        message = f'Ваш код для регистрации:\n' \
                  f'{code}\n' \
                  f'Спасибо за использование нашего сервиса!'
        from_email = EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, from_email, recipient_list)

    @staticmethod
    def send_reset_password_mail(email, code):
        subject = 'Код для восстановления пароля'
        message = f'Ваш код для восстановления пароля:\n' \
                  f'{code}\n' \
                  f'Спасибо за использование нашего сервиса!'
        from_email = EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, from_email, recipient_list)

