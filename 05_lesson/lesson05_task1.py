from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# отрыть браузер Google Chrome
driver = webdriver.Chrome()

# перейти на страницу
driver.get("http://uitestingplayground.com/classattr")

# найти синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

# кликаем по кнопке
blue_button.click()

# пауза
time.sleep(3)

# закрыть браузер
driver.quit()
