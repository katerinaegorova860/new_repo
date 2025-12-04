import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    delay_input = (By.ID, "delay")
    result_field = (By.CSS_SELECTOR, "div.screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        self.driver.get(self.URL)

    @allure.step("Установить задержку калькулятора: {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        filed = self.driver.find_element(*self.delay_input)
        filed.clear()
        filed.send_keys(str(seconds))

    @allure.step("Нажать на кнопку калькулятора: {value}")
    def click_button(self, value: str) -> None:
        button = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        button.click()

    @allure.step("Получить результат вычисления")
    def get_result(self) -> str:
        with allure.step("Ожидание появления результата '15'"):
            self.wait.until(EC.text_to_be_present_in_element(self.result_field, "15"))
        return self.driver.find_element(*self.result_field).text
