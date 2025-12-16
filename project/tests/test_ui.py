import time
import allure
import pytest
from typing import List

from config.test_data import BOOK_NAME
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.cart_helpers import _add_book_to_cart_helper


def _find_search_input(browser: WebDriver) -> WebElement:
    """Находит поле поиска книги в шапке сайта."""
    return WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//input[@name='search' and @type='text' and contains(@class, 'search-form__input--search')]"
        ))
    )


def _find_search_button(browser: WebDriver) -> WebElement:
    """Находит кнопку поиска (лупу) на сайте."""
    return WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[contains(@aria-label, 'Найти') or contains(@class, 'search-form__button-search')]"
        ))
    )


@pytest.mark.ui
@allure.title("UI: Поиск книги по названию")
@allure.feature("Поиск")
def test_search_book(browser: WebDriver) -> None:
    """Проверка, что поиск по названию книги возвращает список результатов."""
    WAIT = WebDriverWait(browser, 10)

    with allure.step("Вводим название книги в поиск"):
        search_input: WebElement = _find_search_input(browser)
        search_input.click()
        search_input.send_keys(BOOK_NAME)

    with allure.step("Нажимаем кнопку поиска дважды"):
        search_button: WebElement = _find_search_button(browser)
        search_button.click()
        WAIT.until(lambda d: search_input.get_attribute("value") == BOOK_NAME)
        search_button.click()
        WAIT.until(
            lambda d: len(d.find_elements(By.XPATH, "//a[contains(@href, '/product/')]")) > 0
        )

    with allure.step("Проверяем, что появились карточки товаров"):
        results: List[WebElement] = WAIT.until(
            EC.presence_of_all_elements_located((
                By.XPATH,
                "//a[contains(@class,'product-card__title')]"
            ))
        )
        assert len(results) > 0

    with allure.step("Визуальная пауза"):
        time.sleep(3)


@pytest.mark.ui
@allure.title("UI: Добавление товара в корзину")
@allure.story("Корзина")
def test_add_book_to_cart(browser: WebDriver) -> None:
    """Добавление книги BOOK_NAME в корзину через поиск и карточку товара."""
    WAIT = WebDriverWait(browser, 10)

    with allure.step("Вводим название книги в поиск"):
        search_input: WebElement = _find_search_input(browser)
        search_input.click()
        search_input.send_keys(BOOK_NAME)

    with allure.step("Нажимаем кнопку поиска дважды"):
        search_button: WebElement = _find_search_button(browser)
        search_button.click()
        WAIT.until(lambda d: search_input.get_attribute("value") == BOOK_NAME)
        search_button.click()
        WAIT.until(
            lambda d: len(d.find_elements(By.XPATH, "//a[contains(@href, '/product/')]")) > 0
        )

    with allure.step("Открываем первый товар из списка"):
        first_product: WebElement = WAIT.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/product/')]"))
        )
        browser.execute_script("arguments[0].click();", first_product)

    with allure.step("Закрываем всплывашку 18+ если появилась"):
        try:
            modal_yes: WebElement = WAIT.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Да')]"))
            )
            browser.execute_script("arguments[0].click();", modal_yes)
        except Exception:
            pass

    with allure.step("Нажимаем кнопку покупки"):
        buy_button: WebElement = WAIT.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(., 'Купить') or contains(., 'В корзину') or contains(., 'Добавить')]"
            ))
        )
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", buy_button)
        browser.execute_script("arguments[0].click();", buy_button)

    with allure.step("Проверяем, что товар добавлен — кнопка стала 'Оформить'"):
        WAIT.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Оформить')]"))
        )


@pytest.mark.ui
@allure.title("UI: Изменение количества товара в корзине")
@allure.story("Корзина")
def test_change_item_quantity_in_cart(browser: WebDriver) -> None:
    """Проверка увеличения количества товара в корзине до 2."""
    WAIT = WebDriverWait(browser, 10)

    with allure.step("Добавляем книгу в корзину"):
        _add_book_to_cart_helper(browser)

    with allure.step("Открываем корзину через иконку в шапке"):
        cart_button: WebElement = WAIT.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[@aria-label='Корзина']"
            ))
        )
        cart_button.click()

    with allure.step("Увеличиваем количество товара до 2 через кнопку плюс"):
        plus_btn: WebElement = WAIT.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//*[local-name()='svg' and contains(@class, 'chg-ui-input-number__input-control--increment')]"
            ))
        )
        plus_btn.click()

    with allure.step("Проверяем, что количество увеличилось до 2"):
        quantity_input: WebElement = WAIT.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//input[contains(@class, 'chg-ui-input-number__input')]"
            ))
        )
        value: str = quantity_input.get_attribute("value")
        assert value == "2", f"Ожидали количество = 2, но получили {value}"

    with allure.step("Визуальная пауза"):
        time.sleep(3)


@pytest.mark.ui
@allure.title("Сортировка: сначала новые после поиска книги")
@allure.description("Вводим название книги, нажимаем поиск дважды и выбираем сортировку 'Сначала новые'.")
@allure.feature("Фильтры и сортировка")
@allure.severity(allure.severity_level.NORMAL)
def test_sort_by_new_first(browser: WebDriver) -> None:
    """Проверка применения сортировки 'Сначала новые' в результатах поиска."""
    WAIT = WebDriverWait(browser, 10)

    with allure.step("Вводим название книги"):
        search_input: WebElement = _find_search_input(browser)
        search_input.click()
        search_input.send_keys(BOOK_NAME)

    with allure.step("Дважды нажимаем на кнопку поиска"):
        search_button: WebElement = _find_search_button(browser)
        search_button.click()
        WAIT.until(lambda d: search_input.get_attribute("value") == BOOK_NAME)
        search_button.click()

    with allure.step("Ждём появления результатов поиска"):
        WAIT.until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@href, '/product/')]")
            )
        )

    with allure.step("Открываем выпадающий список сортировки 'По популярности'"):
        sort_button: WebElement = WAIT.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(@class, 'chg-app-button')"
                " and .//div[contains(@class, 'app-catalog-sorting')"
                " and contains(normalize-space(.), 'По популярности')]]"
            ))
        )
        sort_button.click()

    with allure.step("Выбираем пункт 'Сначала новые'"):
        WAIT.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//div[contains(@class, 'chg-app-dropdown')]"
            ))
        )

        new_first_option: WebElement = WAIT.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[contains(@class, 'chg-app-dropdown-item')"
                " and contains(normalize-space(.), 'Сначала новые')]"
            ))
        )
        new_first_option.click()

    with allure.step("Визуальная пауза для проверки применения сортировки"):
        time.sleep(3)


@pytest.mark.ui
@allure.title("UI: Переход в раздел 'Каталог' из шапки")
@allure.feature("Навигация")
@allure.severity(allure.severity_level.NORMAL)
def test_open_catalog_from_header(browser: WebDriver) -> None:
    """Проверка перехода в каталог по кнопке в шапке."""
    WAIT = WebDriverWait(browser, 10)

    with allure.step("Находим и нажимаем кнопку 'Каталог' в шапке"):
        catalog_btn: WebElement = WAIT.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(@class, 'catalog-btn')"
                " and contains(@class, 'header-sticky__catalog-menu')]"
            ))
        )
        catalog_btn.click()

    with allure.step("Проверяем, что открылся каталог"):
        WAIT.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//*[contains(@class, 'catalog') or contains(@class, 'app-catalog')"
                " or contains(@class, 'catalog-page')]"
            ))
        )

    with allure.step("Визуальная пауза"):
        time.sleep(3)
