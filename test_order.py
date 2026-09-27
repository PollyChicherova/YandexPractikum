# Чичерова Полина, 47 когорта - Финальный проект. Инженер по тестированию плюс

from api_requests import send_new_order, find_order_by_track
from data import new_order


def test_create_and_find_order_by_track():
    # 1. Создаём новый заказ
    create_response = send_new_order(new_order)
    assert create_response.status_code == 201, (
        f"Не удалось создать заказ: код ответа {create_response.status_code}, "
        f"тело ответа: {create_response.text}"
    )

    # 2. Извлекаем трек-номер созданного заказа
    order_data = create_response.json()
    track_number = order_data.get("track")
    assert track_number, (
        f"В ответе на создание заказа не найден трек-номер, тело ответа: {order_data}"
    )

    # 3. Ищем заказ по полученному треку
    search_response = find_order_by_track(track_number)

    # 4. Проверяем, что заказ найден
    assert search_response.status_code == 200, (
        f"Заказ с треком {track_number} не найден: код ответа {search_response.status_code}, "
        f"тело ответа: {search_response.text}"
    )
