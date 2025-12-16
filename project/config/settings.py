from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

# ======================
# UI
# ======================
UI_BASE_URL: str = "https://www.chitai-gorod.ru/"
BASE_URL: str = UI_BASE_URL
DEFAULT_WAIT_TIMEOUT: int = 10

# ======================
# API
# ======================
API_BASE_URL = "https://web-agr.chitai-gorod.ru/web/api/v1/"


def get_driver() -> WebDriver:
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    driver: WebDriver = webdriver.Chrome(options=chrome_options)
    driver.get(UI_BASE_URL)
    return driver
