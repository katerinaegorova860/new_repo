from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    # Локаторы
    delay_input = (By.ID, "delay")
    result_field = (By.CSS_SELECTOR, "div.screen")

    # Методы действий
    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds):
        filed = self.driver.find_element(*self.delay_input)
        filed.clear()
        filed.send_keys(str(seconds))

    def click_button(self, value):
        # Нажать на кнопку с нужным текстом
        button = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        button.click()

    def get_result(self):
        # Ожидание результата и возвраащет его в текст
        self.wait.until(EC.text_to_be_present_in_element(self.result_field, "15"))
        return self.driver.find_element(*self.result_field).text
