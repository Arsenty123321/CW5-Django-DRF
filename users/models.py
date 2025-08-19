from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Электронная почта', help_text="Укажите почту", unique=True)
    first_name = models.CharField(max_length=100, verbose_name="Имя", help_text="Введите имя", blank=True, null=True)
    tg_chat_id = models.CharField(
        max_length=50, verbose_name="Telegram chat_id", help_text="Укажите Telegram chat_id", blank=True, null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']
