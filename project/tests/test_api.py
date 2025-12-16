import pytest
import allure
from requests.models import Response

from helpers.cart_api import add_to_cart, get_cart, remove_from_cart
from config.headers import HEADERS

PRODUCT_ID: int = 2471823


@pytest.fixture(autouse=True)
def clear_cart_before_tests() -> None:
    """Очищаем корзину перед каждым тестом"""
    cart = get_cart(headers=HEADERS).json()
    for item in cart.get("products", []):
        remove_from_cart(item["goodsId"], headers=HEADERS)


@pytest.mark.api
@allure.story("Корзина")
@allure.title("API: Добавление товара в корзину")
def test_add_to_cart() -> None:
    """Проверяем, что товар добавляется в корзину"""
    with allure.step("Добавляем товар в корзину"):
        response: Response = add_to_cart(PRODUCT_ID, headers=HEADERS)
        assert response.status_code == 200, "Не удалось добавить товар в корзину"

    with allure.step("Проверяем, что товар появился в корзине"):
        cart = get_cart(headers=HEADERS).json()
        assert any(item["goodsId"] == PRODUCT_ID for item in cart.get("products", [])), \
            "Товар не найден в корзине"


@pytest.mark.api
@allure.story("Корзина")
@allure.title("API: Количество товара после добавления равно 1")
def test_add_to_cart_quantity_is_one() -> None:
    """Проверяем, что количество товара при добавлении равно 1"""
    with allure.step("Добавляем товар"):
        add_to_cart(PRODUCT_ID, headers=HEADERS)

    with allure.step("Проверяем количество товара в корзине"):
        cart = get_cart(headers=HEADERS).json()
        matching_items = [i for i in cart.get("products", []) if i["goodsId"] == PRODUCT_ID]
        assert matching_items, "Товар не найден в корзине"
        assert matching_items[0]["quantity"] == 1, "Количество товара не равно 1"


@pytest.mark.api
@allure.story("Корзина")
@allure.title("API: Корзина не пуста после добавления товара")
def test_cart_is_not_empty_after_add() -> None:
    """Проверяем, что корзина не пуста после добавления товара"""
    with allure.step("Добавляем товар"):
        add_to_cart(PRODUCT_ID, headers=HEADERS)

    with allure.step("Проверяем, что корзина не пуста"):
        cart = get_cart(headers=HEADERS).json()
        assert len(cart.get("products", [])) > 0, "Корзина пуста после добавления товара"


@pytest.mark.api
@allure.story("Корзина")
@allure.title("API: Общая стоимость корзины больше 0 после добавления товара")
def test_cart_total_cost_after_add() -> None:
    """Проверяем, что общая стоимость корзины больше 0 после добавления товара"""
    with allure.step("Добавляем товар"):
        add_to_cart(PRODUCT_ID, headers=HEADERS)

    with allure.step("Вычисляем общую стоимость корзины"):
        cart = get_cart(headers=HEADERS).json()
        total_cost: float = sum(i["price"] * i["quantity"] for i in cart.get("products", []))
        assert total_cost > 0, "Общая стоимость корзины равна 0 после добавления товара"


@pytest.mark.api
@allure.story("Корзина")
@allure.title("API: Удаление товара из корзины")
def test_remove_product_from_cart() -> None:
    """Добавляем товар и удаляем его по id из корзины"""
    with allure.step("Добавляем товар"):
        add_to_cart(PRODUCT_ID, headers=HEADERS)

    with allure.step("Получаем корзину и находим id добавленного товара"):
        cart = get_cart(headers=HEADERS).json()
        cart_item = next((i for i in cart.get("products", []) if i["goodsId"] == PRODUCT_ID), None)
        assert cart_item, "Товар не найден в корзине после добавления"
        cart_item_id: int = cart_item["id"]

    with allure.step("Удаляем товар из корзины"):
        response: Response = remove_from_cart(cart_item_id, headers=HEADERS)
        assert response.status_code in (200, 204), "Не удалось удалить товар из корзины"

    with allure.step("Проверяем, что товара больше нет в корзине"):
        cart_after = get_cart(headers=HEADERS).json()
        assert all(i["goodsId"] != PRODUCT_ID for i in cart_after.get("products", [])), \
            "Товар не был удален из корзины"
