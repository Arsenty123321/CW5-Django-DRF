from django.db import models

from config import settings


class Habit(models.Model):
    """Модель привычки."""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь", help_text="Создатель привычки",
        blank=True, null=True)
    place = models.CharField(
        max_length=255, verbose_name="Место выполнения", help_text="Введите место выполнения привычки"
    )
    time = models.TimeField(verbose_name="Время выполнения", help_text="Введите время выполнения привычки")
    action = models.TextField(verbose_name="Действие", help_text="Введите действие привычки")
    is_pleasant = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки", help_text="Укажите признак приятной привычки"
    )
    linked_habit = models.ForeignKey("self", on_delete=models.SET_NULL, verbose_name="Связанная привычка",
                                     help_text="Укажите связанную привычку", blank=True, null=True)
    periodicity = models.PositiveIntegerField(default=1, verbose_name="Периодичность",
                                              help_text="Укажите периодичность выполнения привычки в днях")
    reward = models.CharField(max_length=255, verbose_name="Вознаграждение",
                              help_text="Укажите вознаграждение за выполнение привычки", blank=True, null=True)
    time_to_complete = models.PositiveIntegerField(default=120, verbose_name="Время на выполнение",
                                                   help_text="Укажите время на выполнение привычки")
    is_public = models.BooleanField(
        default=False, verbose_name="Признак публичность", help_text="Укажите признак публичности"
    )

    class Meta:
        verbose_name = ("Привычка",)
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"Я буду {self.action}, в {self.place}, в {self.time}"
