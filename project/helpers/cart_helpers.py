import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.test_data import BOOK_NAME


def _search_and_open_book(browser: WebDriver, book_name: str = BOOK_NAME) -> None:
    WAIT = WebDriverWait(browser, 10)
    with allure.step(f"Ищем книгу '{book_name}'"):
        search_input: WebElement = WAIT.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='search' and contains(@class, 'search-form__input--search')]"))
        )
        search_input.click()
        search_input.clear()
        search_input.send_keys(book_name)

        search_button: WebElement = WAIT.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Найти') or contains(@class, 'search-form__button-search')]"))
        )
        search_button.click()
        WAIT.until(lambda d: search_input.get_attribute("value") == book_name)
        search_button.click()
        WAIT.until(lambda d: len(d.find_elements(By.XPATH, "//a[contains(@href, '/product/')]")) > 0)

    with allure.step("Открываем первый товар из списка"):
        first_product = browser.find_elements(By.XPATH, "//a[contains(@href, '/product/')]")[0]
        browser.execute_script("arguments[0].click();", first_product)

    with allure.step("Закрываем 18+ всплывашку если есть"):
        try:
            modal_yes: WebElement = WAIT.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Да')]"))
            )
            browser.execute_script("arguments[0].click();", modal_yes)
        except Exception:
            pass


def _add_book_to_cart_helper(browser: WebDriver, book_name: str = BOOK_NAME) -> None:
    _search_and_open_book(browser, book_name)
    WAIT = WebDriverWait(browser, 10)
    with allure.step("Нажимаем кнопку покупки на карточке товара"):
        buy_button: WebElement = WAIT.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Купить') or contains(., 'В корзину') or contains(., 'Добавить')]"))
        )
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", buy_button)
        browser.execute_script("arguments[0].click();", buy_button)
        WAIT.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Оформить')]")))
