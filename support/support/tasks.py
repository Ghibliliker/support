from django.core.mail import send_mail

from support.celery import app
from support.settings import EMAIL_HOST_USER


@app.task
def send_mail_user(mail_user):
    send_mail(
        'Оповещение от поддержки',
        'Статус вашего тикета был изменён.',
        f'{EMAIL_HOST_USER}',
        [f'{mail_user}'],
        fail_silently=False,
    )
