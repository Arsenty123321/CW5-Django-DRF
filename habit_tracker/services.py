import requests

from config import settings


def send_tg_message(tg_chat_id, message):
    """Отправка сообщения в телеграм."""
    params = {"chat_id": tg_chat_id, "text": message}
    requests.get(f"{settings.TG_URL}{settings.TG_BOT_TOKEN}/sendMessage", params=params)
