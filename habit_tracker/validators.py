from rest_framework.exceptions import ValidationError


class HabitValidator:
    """Валидатор полей модели привычки."""

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        time_to_complete = value.get("time_to_complete")
        if time_to_complete < 1 or time_to_complete > 120:
            raise ValidationError("Время выполнения не может быть меньше 1 секунды и превышать 120 секунд")

        if value.get("linked_habit") and value.get("reward"):
            raise ValidationError("Нельзя выбирать одновременно связанную привычку и вознаграждение")

        if value.get("linked_habit"):
            if not value.get("linked_habit").is_pleasant:
                raise ValidationError("Связанная привычка должна быть с признаком приятной привычки")

        if value.get("is_pleasant"):
            if value.get("linked_habit") or value.get("reward"):
                raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")

        periodicity = value.get("periodicity")
        if periodicity < 1 or periodicity > 7:
            raise ValidationError("Привычка должна выполняться хотя бы один раз и не реже чем раз в 7 дней")
