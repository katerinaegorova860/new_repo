import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Страница корзины.
    """
    def __init__(self, driver):
        """
        Инициализация страницы корзины.
        :param driver: WebDriver
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self) -> None:
        """Нажимает кнопку Checkout."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()
