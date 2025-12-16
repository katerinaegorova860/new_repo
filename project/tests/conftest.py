import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config.settings import get_driver, UI_BASE_URL


@pytest.fixture
def browser():
    driver = get_driver()
    try:
        wait = WebDriverWait(driver, 10)
        btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'chg-app-button__content') and (contains(text(),'Да') or contains(text(),'здесь'))]"))
        )
        btn.click()
    except Exception:
        pass
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def auth_headers():
    TOKEN = "eyJhbGciOiJI..."
    return {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
