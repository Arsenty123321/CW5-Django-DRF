from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit_tracker.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="user1@users.ru")
        self.habit = Habit.objects.create(
            owner=self.user, place="Test place", time="10:00:00", action="Test action")
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        """Тест создания привычки."""
        url = reverse("habits:habit-create")
        data = {
            "place": "Test place2",
            "time": "11:00:00",
            "action": "Test action2",
            "time_to_complete": 100,
            "periodicity": 7,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_delete(self):
        """Тест удаления привычки."""
        url = reverse("habits:habit-delete", args=(self.habit.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_update(self):
        """Тест обновления привычки."""
        url = reverse("habits:habit-update", args=(self.habit.pk,))
        data = {"place": "Test new place", "time_to_complete": 120, "periodicity": 1}
        response = self.client.patch(url, data)
        new_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_data.get("place"), data.get("place"))

    def test_habit_retrieve(self):
        """Тест просмотра одной привычки."""
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("owner"), self.habit.owner.id)

    def test_habit_list(self):
        """Тест просмотра списка привычек пользователя."""
        url = reverse("habits:habits-list")
        response = self.client.get(url)
        data = response.json().get("results")[0]
        result = {
            "id": self.habit.id,
            "place": self.habit.place,
            "time": self.habit.time,
            "action": self.habit.action,
            "is_pleasant": self.habit.is_pleasant,
            "periodicity": self.habit.periodicity,
            "reward": self.habit.reward,
            "time_to_complete": self.habit.time_to_complete,
            "is_public": self.habit.is_public,
            "owner": self.habit.owner.id,
            "linked_habit": self.habit.linked_habit,
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_public_list(self):
        """Тест просмотра публичных привычек."""
        url = reverse("habits:habits-public-list")
        response = self.client.get(url)
        data = response.json()
        result = {"count": 0, "next": None, "previous": None, "results": []}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_wrong_create_reward_linked_habit(self):
        """Тест невозможности создания привычки при одновременном выборе связанной привычки и вознаграждения"""
        url = reverse("habits:habit-create")
        wrong_habit_data = {
            "place": "Test place2",
            "time": "11:00:00",
            "action": "Test action2",
            "time_to_complete": 10,
            "periodicity": 7,
            "reward": "Reward mmm...",
            "linked_habit": self.habit.id,
        }
        response = self.client.post(url, wrong_habit_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["Нельзя выбирать одновременно связанную привычку и вознаграждение"], )

    def test_wrong_create_is_pleasant_with_reward(self):
        """Тест невозможности создания приятной привычки с указанием вознаграждения"""
        url = reverse("habits:habit-create")
        wrong_habit_data = {
            "place": "Test place2",
            "time": "11:00:00",
            "action": "Test action2",
            "time_to_complete": 100,
            "periodicity": 7,
            "is_pleasant": True,
            "reward": "Reward mmm...",
        }
        response = self.client.post(url, wrong_habit_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["У приятной привычки не может быть вознаграждения или связанной привычки"],
        )

    def test_wrong_create_is_pleasant_with_linked_habit(self):
        """Тест невозможности создания приятной привычки и связи с другой привычкой"""
        habit2 = Habit.objects.create(
            owner=self.user, place="Test placeX", time="12:00:00", action="Test actionX", is_pleasant=True)
        url = reverse("habits:habit-create")
        wrong_habit_data = {
            "place": "Test place2",
            "time": "11:00:00",
            "action": "Test action2",
            "time_to_complete": 100,
            "periodicity": 7,
            "is_pleasant": True,
            "linked_habit": habit2.id,
        }
        response = self.client.post(url, wrong_habit_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["У приятной привычки не может быть вознаграждения или связанной привычки"],
        )

    def test_wrong_create_normal_habit_with_linked_normal_habit(self):
        """Тест невозможности создания обычной привычки и связи с другой обычной привычкой"""
        url = reverse("habits:habit-create")
        wrong_habit_data = {
            "place": "Test place2",
            "time": "11:00:00",
            "action": "Test action2",
            "time_to_complete": 100,
            "periodicity": 7,
            "is_pleasant": False,
            "linked_habit": self.habit.id,
        }
        response = self.client.post(url, wrong_habit_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["Связанная привычка должна быть с признаком приятной привычки"],
        )
