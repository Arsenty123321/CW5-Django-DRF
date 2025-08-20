from rest_framework import serializers

from habit_tracker.models import Habit
from habit_tracker.validators import HabitValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [HabitValidator(fields="__all__")]
