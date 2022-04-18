from django.db import models
from django.db.models.deletion import CASCADE

from users.models import User


class Ticket(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active'
        COMPLITE = 'complite'
        FROZEN = 'frozen'

    name = models.TextField(verbose_name='имя тикета')
    text = models.TextField(
        verbose_name='текст тикета',
        help_text='Напишите текст',
    )
    image = models.ImageField(
        'Картинка',
        upload_to='tickets/',
        blank=True, null=True
    )
    status = models.CharField(
        verbose_name='статус тикета',
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
    author = models.ForeignKey(
        User,
        on_delete=CASCADE,
        verbose_name='автор тикета',
        related_name='tickets'
    )
    pub_date = models.DateTimeField('дата создания тикета', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Тикет'
        verbose_name_plural = 'Тикеты'


class Comment(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        verbose_name='коммент тикета',
        related_name='comments'
    )
    text = models.TextField(
        verbose_name='текст комментария',
        blank=False,
        help_text='Напишите комментарий',
    )
    image = models.ImageField('Картинка', upload_to='tickets/', blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор комментария',
        related_name='comments'
    )
    pub_date = models.DateTimeField('дата комментария', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
