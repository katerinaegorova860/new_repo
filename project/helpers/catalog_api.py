# helpers/catalog_api.py
import requests
from config.settings import API_BASE_URL


def get_product_by_id(product_id: int, headers: dict | None = None):
    """
    Получение карточки товара по id.
    GET /products/<product_id>
    """
    url = f"{API_BASE_URL}products/{product_id}"
    return requests.get(url, headers=headers, timeout=10)
