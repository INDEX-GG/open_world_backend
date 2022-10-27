from django.core.mail import send_mail
from altay_backend.config import EMAIL_HOST_USER


class Util:
    @staticmethod
    def send_feedback_mail(data):
        municipality = data['municipality']
        family_status = data['family_status']
        child_age = data['child_age']
        disabled_person = data['disabled_person']
        limited_person = data['limited_person']
        specialist = data['specialist']
        counseling_theme = data['counseling_theme']
        other = data['other']
        phone = data['phone']
        email = data['email']

        subject = 'Обратная связь'
        message = f'Наименование муниципального образования: {municipality}\n' \
                  f'Статус семьи: {family_status}\n' \
                  f'Возраст ребёнка: {child_age}\n' \
                  f'Наличие в семье ребенка-инвалида: {disabled_person}\n' \
                  f'Наличие в семье ребенка с ограниченными возможностями здоровья: {limited_person}\n' \
                  f'Выбор специалиста для консультирования: {specialist}\n' \
                  f'Тема консультирования: {counseling_theme}\n' \
                  f'Другое: {other}\n' \
                  f'Номер телефона: {phone}\n' \
                  f'Адрес электронной почты: {email}\n' \
                  f'Спасибо за обращение!'
        from_email = EMAIL_HOST_USER
        recipient_list = ['go_2002@mail.ru', ]
        send_mail(
            subject,
            message,
            from_email,
            recipient_list)
