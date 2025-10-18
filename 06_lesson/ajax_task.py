from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открыть браузер (Chrome)
driver = webdriver.Chrome()

# Перейти на страницу
driver.get("http://uitestingplayground.com/ajax")

# Нажать на синюю кнопку
blue_button = driver.find_element(By.ID, "ajaxButton")
blue_button.click()

# Явное ожидание появления зеленой плашки с текстом
wait = WebDriverWait(driver, 20)
green_message = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
)

print(green_message.text)

driver.quit()
