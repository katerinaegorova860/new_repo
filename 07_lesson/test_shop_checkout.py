import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Pages.pages import LoginPage, MainPage, CartPage, CheckoutPage


def test_complete_purchase_flow():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Авторизация
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Главная страница - добавление товаров
    main_page = MainPage(driver)
    main_page.add_product_to_cart("Sauce Labs Backpack")
    main_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
    main_page.add_product_to_cart("Sauce Labs Onesie")
    main_page.go_to_cart()

    # Корзина
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Оформление заказа
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Kate", "Ivanova", "12345")
    checkout_page.click_continue()
    total = checkout_page.get_total()

    # Проверка итоговой суммы
    assert total == 58.29

    driver.quit()
