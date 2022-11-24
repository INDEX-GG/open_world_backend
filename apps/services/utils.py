from django.core.mail import send_mail

from config.config import EMAIL_HOST_USER, EMAIL_RECIPIENT


class Util:
    @staticmethod
    def send_services_offline_mail(data):
        subject = 'Оффлайн консультация'
        message = f'Услуга: {data["services_name"]}\n' \
                  f'ФИО: {data["name"]} {data["lastname"]} {data["patronymic"]}\n' \
                  f'Адрес электронной почты: {data["email"]}\n' \
                  f'Номер телефона: {data["phone"]}\n' \
                  f'Вопрос: {data["question"]}\n' \
                  f'Способ связи: {data["communication"]}\n'
        from_email = EMAIL_HOST_USER
        recipient_list = [EMAIL_RECIPIENT, ]
        result = send_mail(subject, message, from_email, recipient_list)
        return result

    @staticmethod
    def send_services_video_mail(data):
        subject = 'Видео консультация'
        message = f'Услуга: {data["services_name"]}\n' \
                  f'ФИО: {data["name"]} {data["lastname"]} {data["patronymic"]}\n' \
                  f'Адрес электронной почты: {data["email"]}\n' \
                  f'Вопрос: {data["question"]}\n'
        from_email = EMAIL_HOST_USER
        recipient_list = [EMAIL_RECIPIENT, ]
        result = send_mail(subject, message, from_email, recipient_list)
        return result
