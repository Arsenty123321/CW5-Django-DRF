from rest_framework import generics

from habit_tracker.models import Habit
from habit_tracker.paginations import HabitsPagination
from habit_tracker.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitListAPIView(generics.ListAPIView):
    """Отображение списка привычек."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user).order_by('id')


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Отображение информации о привычке."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_permissions(self):
        self.permission_classes = [IsOwner]
        return super().get_permissions()


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Обновление привычки."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_permissions(self):
        self.permission_classes = [IsOwner]
        return super().get_permissions()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_permissions(self):
        self.permission_classes = [IsOwner]
        return super().get_permissions()


class HabitPublicListAPIView(generics.ListAPIView):
    """Отображение списка публичных привычек."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination

    def get_queryset(self):
        return Habit.objects.filter(is_public=True).order_by('id')
