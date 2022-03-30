from Config.config import Test_Data
from Pages.base_page import Base_Page
from Locators import login_page_locators as locator


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
        self.send_text(locator.EMAIL, username)
        self.send_text(locator.PASSWORD, password)
        self.click(locator.LOGIN_BUTTON)
