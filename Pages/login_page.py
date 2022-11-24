from Configurations.config import TestData
from Pages.base_page import BasePage
from Locators.login_page_locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # Page Actions:
    def get_login_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.send_text(LoginLocators.EMAIL, username)
        self.send_text(LoginLocators.PASSWORD, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def invalid_login(self, username, invalid_password):
        self.send_text(LoginLocators.EMAIL, username)
        self.send_text(LoginLocators.PASSWORD, invalid_password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def go_to(self):
        self.driver.get(TestData.BASE_URL)
