import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Страница калькулятора.
    """
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        """
        Инициализация страницы.
        :param driver: WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    delay_input = (By.ID, "delay")
    result_field = (By.CSS_SELECTOR, "div.screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(self.URL)

    @allure.step("Установить задержку калькулятора: {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """Устанавливает задержку вычислений калькулятора."""
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(str(seconds))

    @allure.step("Нажать на кнопку калькулятора: {value}")
    def click_button(self, value: str) -> None:
        """Нажимает кнопку калькулятора с указанным значением."""
        button = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        button.click()

    @allure.step("Получить результат вычисления")
    def get_result(self) -> str:
        """Возвращает текст результата с калькулятора."""
        self.wait.until(EC.text_to_be_present_in_element(self.result_field, "15"))
        return self.driver.find_element(*self.result_field).text
