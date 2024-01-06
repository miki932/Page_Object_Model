from selenium.webdriver.common.by import By
from Configurations import config
from Pages.base_page import BasePage
from logger import logger


class LoginPage(BasePage):
    # Locators:
    LOGIN_PAGE_TITLE = "Swag Labs"
    EMAIL = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LOCKED_OUT_ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    BAD_PASSWORD_OR_USERNAME_ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")

    # Page Actions:
    def __init__(self, driver):
        super().__init__(driver)

    def go_to(self):
        logger.info(f"Navigating to: {config.BASE_URL}")
        self.driver.get(config.BASE_URL)

    def get_login_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.go_to()
        self.send_text(LoginPage.EMAIL, username)
        self.send_text(LoginPage.PASSWORD, password)
        self.click(LoginPage.LOGIN_BUTTON)

    def invalid_login(self, username, invalid_password):
        self.send_text(LoginPage.EMAIL, username)
        self.send_text(LoginPage.PASSWORD, invalid_password)
        self.click(LoginPage.LOGIN_BUTTON)
