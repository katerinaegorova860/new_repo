import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить форму Checkout: {first_name} {last_name}, {postal_code}")
    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
        ).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name_input)
        ).send_keys(last_name)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.postal_code_input)
        ).send_keys(postal_code)

    @allure.step("Нажать Continue")
    def click_continue(self) -> None:
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    @allure.step("Получить итоговую сумму заказа")
    def get_total(self) -> float:
        total_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_label)
        ).text
        return float(total_text.replace("Total: $", ""))
