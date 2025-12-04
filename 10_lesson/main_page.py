import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Добавить товар в корзину: {product_name}")
    def add_product_to_cart(self, product_name: str) -> None:
        product_id = product_name.lower().replace(" ", "-")
        button_id = f"add-to-cart-{product_id}"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, button_id))
        ).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
        ).click()
