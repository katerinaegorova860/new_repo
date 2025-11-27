from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

# Установка Firefox через webdriver-manager
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("http://the-internet.herokuapp.com/inputs")

# Найти поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")

# Ввести текст Sky
input_field.send_keys("Sky")
time.sleep(1)

# Очистить поле
input_field.clear()
time.sleep(1)

# Ввести текст Pro
input_field.send_keys("Pro")
time.sleep(2)

# Закрыть браузер
driver.quit()
