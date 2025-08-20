from django.urls import path

from habit_tracker.apps import HabitTrackerConfig
from habit_tracker.views import HabitListAPIView, HabitRetrieveAPIView, HabitCreateAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, HabitPublicListAPIView

app_name = HabitTrackerConfig.name

urlpatterns = [
    path("habits/", HabitListAPIView.as_view(), name="habits-list"),
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit-detail"),
    path("habits/create/", HabitCreateAPIView.as_view(), name="habit-create"),
    path("habits/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit-update"),
    path("habits/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit-delete"),
    path("public_habits/", HabitPublicListAPIView.as_view(), name="habits-public-list"),
]
