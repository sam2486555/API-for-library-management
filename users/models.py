from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='E-mail пользователя',
        help_text='Введите E-mail пользователя'
    )
    password = models.CharField(
        max_length=100,
        verbose_name='Пароль',
        help_text='Введите пароль'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
