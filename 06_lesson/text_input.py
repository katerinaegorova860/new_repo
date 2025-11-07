from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# открыть браузер
driver = webdriver.Chrome()

# перейти на сайт
driver.get("http://uitestingplayground.com/textinput")

# найти поле ввода и ввести текст
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

# найти синюю кнопку и кликнуть по ней
button = driver.find_element(By.ID, "updatingButton")
button.click()

# явное ожиданиеБ пока текст кнопки не изменится на "SkyPro"
wait = WebDriverWait(driver, 10)
wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro"))

# получить текст кнопки
button_text = button.text
print(button_text)

# закрыть сайт
driver.quit()
