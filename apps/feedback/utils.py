from django.core.mail import send_mail

from config.config import EMAIL_HOST_USER, EMAIL_RECIPIENT, EMAIL_RECIPIENT_WEB


class Util:
    @staticmethod
    def send_feedback_mail(data):
        for i in data:
            if data[i] == '':
                data[i] = 'Не указано'
            else:
                continue

        subject = 'Обратная связь'
        message = f'Способ связи: {data["communication"]}\n' \
                  f'Наименование муниципального образования: {data["municipality"]}\n' \
                  f'Статус семьи: {data["family_status"]}\n' \
                  f'Возраст ребёнка: {data["child_age"]}\n' \
                  f'Наличие в семье ребенка-инвалида: {data["disabled_person"]}\n' \
                  f'Наличие в семье ребенка с ограниченными возможностями здоровья: {data["limited_person"]}\n' \
                  f'Выбор специалиста для консультирования: {data["specialist"]}\n' \
                  f'Тема консультирования: {data["counseling_theme"]}\n' \
                  f'Другое: {data["other"]}\n' \
                  f'Номер телефона: {data["phone"]}\n' \
                  f'Адрес электронной почты: {data["email"]}\n'
        from_email = EMAIL_HOST_USER
        recipient_list = [EMAIL_RECIPIENT, ]
        result = send_mail(subject, message, from_email, recipient_list)
        return result


class SendFeedbackMessage:
    @staticmethod
    def send_feedback_mail(data):
        for i in data:
            if data[i] == '':
                data[i] = 'Не указано'
            else:
                continue

        subject = 'Обратная связь'
        message = f'Имя: {data["name"]}\n' \
                  f'Адрес электронной почты: {data["email"]}\n' \
                  f'Номер телефона: {data["phone"]}\n' \
                  f'Сообщение: {data["message"]}\n'
        from_email = EMAIL_HOST_USER
        recipient_list = [EMAIL_RECIPIENT_WEB, ]
        result = send_mail(subject, message, from_email, recipient_list)
        return result
