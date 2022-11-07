from django.core.mail import send_mail
from altay_backend.config import EMAIL_HOST_USER, EMAIL_RECIPIENT


class Util:
    @staticmethod
    def send_services_offline_mail(data):
        services_name = data['services_name']
        name = data['name']
        lastname = data['lastname']
        patronymic = data['patronymic']
        email = data['email']
        phone = data['phone']
        question = data['question']
        communication = data['communication']

        subject = 'Оффлайн консультация'
        message = f'Услуга: {services_name}\n' \
                  f'ФИО: {name} {lastname} {patronymic}\n' \
                  f'Адрес электронной почты: {email}\n' \
                  f'Номер телефона: {phone}\n' \
                  f'Вопрос: {question}\n' \
                  f'Способ связи: {communication}\n'
        from_email = EMAIL_HOST_USER
        recipient_list = [EMAIL_RECIPIENT, ]
        result = send_mail(subject, message, from_email, recipient_list)
        return result

    @staticmethod
    def send_services_video_mail(data):
        services_name = data['services_name']
        name = data['name']
        lastname = data['lastname']
        patronymic = data['patronymic']
        email = data['email']
        question = data['question']
        subject = 'Видео консультация'
        message = f'Услуга: {services_name}\n' \
                  f'ФИО: {name} {lastname} {patronymic}\n' \
                  f'Адрес электронной почты: {email}\n' \
                  f'Вопрос: {question}\n'
        from_email = EMAIL_HOST_USER
        recipient_list = [EMAIL_RECIPIENT, ]
        result = send_mail(subject, message, from_email, recipient_list)
        return result
