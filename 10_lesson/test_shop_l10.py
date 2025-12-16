import pytest
import allure
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.feature("Shop")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Покупка одного товара")
@allure.description("Добавить товара в корзину и оформления заказа")
def test_buy_product():
    driver = webdriver.Chrome()
    login = LoginPage(driver)
    main = MainPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    try:
        with allure.step("Открыть главную страницу магазина"):
            driver.get("https://www.saucedemo.com/")

        with allure.step("Ввести логин и пароль и кликнуть вход"):
            login.enter_username("standard_user")
            login.enter_password("secret_sauce")
            login.click_login()

        with allure.step("Добавить товар в корзину и перейти в корзину"):
            main.add_product_to_cart("Sauce Labs Backpack")
            main.go_to_cart()

        with allure.step("Нажать Checkout"):
            cart.click_checkout()

        with allure.step("Заполнить форму Checkout и продолжить"):
            checkout.fill_form("Иван", "Иванов", "12345")
            checkout.click_continue()

        with allure.step("Проверить итоговую сумму заказа"):
            total = checkout.get_total()
            assert total > 0, f"Ожидалось, что сумма больше 0, получили {total}"

    finally:
        driver.quit()
