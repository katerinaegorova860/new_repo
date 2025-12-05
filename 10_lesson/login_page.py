import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Страница входа в систему.
    """
    def __init__(self, driver):
        """
        Инициализация страницы Login.
        :param driver: WebDriver
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> None:
        """Вводит имя пользователя."""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    @allure.step("Ввести пароль: {password}")
    def enter_password(self, password: str) -> None:
        """Вводит пароль."""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(password)

    @allure.step("Нажать кнопку входа")
    def click_login(self) -> None:
        """Нажимает кнопку Login."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()
