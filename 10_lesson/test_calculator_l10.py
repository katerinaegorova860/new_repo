import pytest
import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка сложения в калькуляторе")
@allure.description("Тест проверяет, что калькулятор правильно считает 10 + 5")
def test_sum_calculator():
    driver = webdriver.Chrome()
    calc_page = CalculatorPage(driver)

    try:
        calc_page.open()
        calc_page.set_delay(0)

        with allure.step("Нажимаем кнопки 1, 0, +, 5, ="):
            calc_page.click_button("1")
            calc_page.click_button("0")
            calc_page.click_button("+")
            calc_page.click_button("5")
            calc_page.click_button("=")

        with allure.step("Проверяем результат"):
            result = calc_page.get_result()
            assert result == "15", f"Ожидалось 15, но получили {result}"

    finally:
        driver.quit()
