from datetime import datetime
from celery import shared_task
from habit_tracker.models import Habit
from habit_tracker.services import send_tg_message


@shared_task
def habits_reminder():
    """
        Проверка и отправка тех привычек, которые подходят по времени.
        Если у владельца не указан tg_chat_id, то отправка пропускается.
    """
    time_now = datetime.now()
    habits = Habit.objects.filter(is_pleasant=False)

    for habit in habits:
        tg_chat_id = habit.owner.tg_chat_id
        if tg_chat_id is not None:
            if time_now.hour == habit.time.hour and time_now.minute == habit.time.minute:
                message = f"Есть отличная привычка: {habit.action} в {habit.time} в {habit.place}"
                send_tg_message(tg_chat_id=tg_chat_id, message=message)
