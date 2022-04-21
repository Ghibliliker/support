from django.core.mail import send_mail

from support.celery import app
from support.settings import EMAIL_HOST_USER


@app.task
def send_mail_user(mail_user: str) -> None:
    """Send mail to user about ticket status"""
    send_mail(
        'Support alert',
        'Your ticket status has changed.',
        f'{EMAIL_HOST_USER}',
        [f'{mail_user}'],
        fail_silently=False,
    )
