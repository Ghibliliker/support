from django.db import models
from django.db.models.deletion import CASCADE

from users.models import User


class Ticket(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active'
        COMPLITE = 'complite'
        FROZEN = 'frozen'

    name = models.TextField(verbose_name='ticket name')
    text = models.TextField(
        verbose_name='ticket text',
        help_text='write text',
    )
    image = models.ImageField(
        'image',
        upload_to='tickets/',
        blank=True, null=True
    )
    status = models.CharField(
        verbose_name='ticket status',
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
    author = models.ForeignKey(
        User,
        on_delete=CASCADE,
        verbose_name='ticket author',
        related_name='tickets'
    )
    pub_date = models.DateTimeField('ticket creation date', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'


class Comment(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        verbose_name='ticket comment',
        related_name='comments'
    )
    text = models.TextField(
        verbose_name='text comment',
        blank=False,
        help_text='write text',
    )
    image = models.ImageField('image', upload_to='tickets/', blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='comment author',
        related_name='comments'
    )
    pub_date = models.DateTimeField('comment creation date', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
