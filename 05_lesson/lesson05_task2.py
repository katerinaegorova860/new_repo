from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# открыть браузер Google Chrome
driver = webdriver.Chrome()

# переходим на страницу
driver.get("http://uitestingplayground.com/dynamicid")

# найти синюю кнопку по XPath с использованием текста,
# так как ее id каждый раз меняется (динамический)
blue_button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")

# кликнуть по кнопке
blue_button.click()

# пауза
time.sleep(3)

# закрыть браузер
driver.quit()
