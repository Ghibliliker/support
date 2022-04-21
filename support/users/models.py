from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=100, unique=True,
        blank=True, verbose_name='user username')
    email = models.EmailField(
        blank=True, unique=True, verbose_name='user email')
    first_name = models.CharField(
        max_length=100, verbose_name='user first name')
    last_name = models.CharField(
        max_length=100, verbose_name='user last name')
    is_support = models.BooleanField(
        verbose_name='support user',
        default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
