from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait = WebDriverWait(driver, 10)

    # Ждать, пока поле "First name" появится на странице
    wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

    # Заполнить поля
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # zip-code оставить пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажать кнопку Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Ждать, когда загрузится страница с результатом (div.alert вместо input)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.alert")))

    # Проверить зелёные поля
    success_fields = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field in success_fields:
        elem = driver.find_element(By.ID, field)
        assert "alert-success" in elem.get_attribute("class"), f"Поле {field} не зелёное"
        print(f"{field} — зелёное")

    # Проверить красное поле
    zip_field = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_field.get_attribute("class"), "Zip code не красное"
    print("zip-code — красное (ошибка)")

    driver.quit()
