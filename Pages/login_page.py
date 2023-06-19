from Configurations import config
from Pages.base_page import BasePage
from Locators.login_page_locators import LoginLocators


class LoginPage(BasePage):
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
        self.driver.get(config.BASE_URL)
