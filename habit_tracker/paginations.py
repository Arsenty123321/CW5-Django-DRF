from rest_framework.pagination import PageNumberPagination


class HabitsPagination(PageNumberPagination):
    """Пагинация списка привычек."""

    page_size = 5
