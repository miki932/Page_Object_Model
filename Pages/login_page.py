from Config.config import Test_Data
from Pages.base_page import Base_Page
from Locators.login_page_locators import Login_Locators


class Login_Page(Base_Page):

    # It is necessary to initialize the driver as a page class member for implement Page Factory.
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Test_Data.BASE_URL)

    # Page Actions:
    def get_login_title(self, title):
        return self.get_title(title)

    def is_signup_link_visible(self):
        return self.is_visible(self.SIGNUP_LINK)

    def do_login(self, username, password):
        self.send_text(Login_Locators.EMAIL, username)
        self.send_text(Login_Locators.PASSWORD, password)
        self.click(Login_Locators.LOGIN_BUTTON)

    def invalid_login(self, username, invalid_password):
        self.send_text(Login_Locators.EMAIL, username)
        self.send_text(Login_Locators.PASSWORD, invalid_password)
        self.click(Login_Locators.LOGIN_BUTTON)
