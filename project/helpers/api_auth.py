from typing import Dict
from selenium.webdriver.remote.webdriver import WebDriver


def get_auth_cookies(driver: WebDriver) -> Dict[str, str]:
    """
    Получает cookies из браузера для API-запросов.

    :param driver: Selenium WebDriver
    :return: словарь cookies
    """
    return {cookie["name"]: cookie["value"] for cookie in driver.get_cookies()}


def get_auth_headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}"
    }
