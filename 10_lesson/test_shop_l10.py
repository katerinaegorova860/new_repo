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
@allure.description("Тест проверяет процесс добавления товара в корзину и оформления заказа")
def test_buy_product():
    driver = webdriver.Chrome()
    login = LoginPage(driver)
    main = MainPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    try:
        driver.get("https://www.saucedemo.com/")  # пример сайта

        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

        main.add_product_to_cart("Sauce Labs Backpack")
        main.go_to_cart()

        cart.click_checkout()

        checkout.fill_form("Иван", "Иванов", "12345")
        checkout.click_continue()

        with allure.step("Проверяем итоговую сумму"):
            total = checkout.get_total()
            assert total > 0, f"Ожидалось, что сумма больше 0, получили {total}"

    finally:
        driver.quit()
