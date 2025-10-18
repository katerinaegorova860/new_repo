from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер
driver = webdriver.Chrome()

# Переходим на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Явное ожидание — ждём, пока загрузятся все 4 картинки
WebDriverWait(driver, 15).until(
    lambda d: len(d.find_elements(By.CSS_SELECTOR, "#image-container img")) == 4
)
images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

# Получаем атрибут у 3-й картинки
third_image_src = images[2].get_attribute("src")

# Выводим в консоль
print(third_image_src)

# Закрываем браузер
driver.quit()
