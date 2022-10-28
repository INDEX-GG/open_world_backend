from django.core.mail import send_mail
from altay_backend.config import EMAIL_HOST_USER


class Util:
    @staticmethod
    def send_feedback_mail(data):
        if data['municipality'] != '':
            municipality = data['municipality']
        else:
            municipality = 'Не указано'

        if data['family_status'] != '':
            family_status = data['family_status']
        else:
            family_status = 'Не указано'

        if data['child_age'] != '':
            child_age = data['child_age']
        else:
            child_age = 'Не указано'

        if data['disabled_person'] != '':
            disabled_person = data['disabled_person']
        else:
            disabled_person = 'Не указано'

        if data['limited_person'] != '':
            limited_person = data['limited_person']
        else:
            limited_person = 'Не указано'

        if data['specialist'] != '':
            specialist = data['specialist']
        else:
            specialist = 'Не указано'

        if data['counseling_theme'] != '':
            counseling_theme = data['counseling_theme']
        else:
            counseling_theme = 'Не указано'

        if data['other'] != '':
            other = data['other']
        else:
            other = 'Не указано'

        if data['phone'] != '':
            phone = data['phone']
        else:
            phone = 'Не указано'

        if data['email'] != '':
            email = data['email']
        else:
            email = 'Не указано'

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
