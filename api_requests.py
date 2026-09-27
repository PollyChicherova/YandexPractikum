# Импорт модуля requests для отправки HTTP-запросов
import requests

# Импорт конфигурационного файла с адресами API
import config


def send_new_order(order):
    """Отправляет POST-запрос на создание нового заказа."""
    return requests.post(config.BASE_URL + config.ORDERS_PATH, json=order)


def find_order_by_track(track_number):
    """Отправляет GET-запрос на поиск заказа по номеру трека."""
    return requests.get(config.BASE_URL + config.ORDER_TRACK_PATH, params={"t": track_number})
