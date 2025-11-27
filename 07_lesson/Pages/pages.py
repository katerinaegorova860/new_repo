from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Страница авторизации
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()


# Главная страница
class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        # Преобразуем название товара в id кнопки
        product_id = product_name.lower().replace(" ", "-")
        button_id = f"add-to-cart-{product_id}"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, button_id))
        ).click()

    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
        ).click()


# Корзина
class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()


# Оформление заказа
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
        ).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name_input)
        ).send_keys(last_name)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.postal_code_input)
        ).send_keys(postal_code)

    def click_continue(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    def get_total(self):
        total_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_label)
        ).text
        return float(total_text.replace("Total: $", ""))
