import random
from django.core.mail import send_mail
from config.config import EMAIL_HOST_USER


class Util:
    @staticmethod
    def generate_code():
        # Generates a random code
        code = random.randint(100000, 999999)
        return code

    @staticmethod
    def send_verification_mail(email, code):
        # Sends the generated random code to the email for registration
        subject = 'Код для регистрации'
        message = f'Ваш код для регистрации:\n' \
                  f'{code}\n' \
                  f'Спасибо за использование нашего сервиса!\n\n' \
                  f'БУ РА «РРЦ»\n' \
                  f'Адрес: Республика Алтай г. Горно-Алтайск пр. Коммунистический, 109\n' \
                  f'Телефон: 8(38822)6-23-01'
        from_email = EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, from_email, recipient_list)

    @staticmethod
    def send_reset_password_mail(email, code):
        # Sends the generated random code to the email for reset password
        subject = 'Код для восстановления пароля'
        message = f'Ваш код для восстановления пароля:\n' \
                  f'{code}\n' \
                  f'Спасибо за использование нашего сервиса!\n\n' \
                  f'БУ РА «РРЦ»\n' \
                  f'Адрес: Республика Алтай г. Горно-Алтайск пр. Коммунистический, 109\n' \
                  f'Телефон: 8(38822)6-23-01'
        from_email = EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, from_email, recipient_list)
