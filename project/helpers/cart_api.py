import requests
from config.settings import API_BASE_URL


def add_to_cart(product_id: int, headers: dict | None = None):
    """
    Добавление товара в корзину.
    POST /cart/product  body: {"id": <product_id>}
    """
    url = f"{API_BASE_URL}cart/product"
    payload = {"id": product_id}
    return requests.post(url, json=payload, headers=headers, timeout=10)


def get_cart(headers: dict | None = None):
    """
    Получение текущей корзины.
    GET /cart
    """
    url = f"{API_BASE_URL}cart"
    return requests.get(url, headers=headers, timeout=10)


def update_cart_item(product_id: int, quantity: int, headers: dict | None = None):
    """
    Изменение количества товара в корзине.
    PUT /cart/product  body: {"id": <product_id>, "quantity": <quantity>}
    """
    url = f"{API_BASE_URL}cart/product"
    payload = {"id": product_id, "quantity": quantity}
    return requests.put(url, json=payload, headers=headers, timeout=10)


def remove_from_cart(product_id: int, headers: dict | None = None):
    """
    Удаление товара из корзины.
    DELETE /cart/product/<product_id>
    """
    url = f"{API_BASE_URL}cart/product/{product_id}"
    return requests.delete(url, headers=headers, timeout=10)
