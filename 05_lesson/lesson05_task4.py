from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Настройка и открытие браузера Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    # 1. Открыть страницу
    driver.get("http://the-internet.herokuapp.com/login")

    # 2. Ввести имя пользователя
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")

    # 3. Ввести пароль
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")

    # 4. Нажать кнопку Login
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # 5. Подождать немного, чтобы страница обновилась
    time.sleep(2)

    # 6. Найти элемент с зелёной плашкой и вывести его текст
    success_message = driver.find_element(By.ID, "flash")
    print(success_message.text)

finally:
    # 7. Закрыть браузер
    driver.quit()
