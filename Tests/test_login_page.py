import current as current

from Pages.base_page import BasePage
from Pages.login_page import LoginPage
from Locators.login_page_locators import LoginLocators
from Config.config import TestData


class TestLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(self.driver)
        self.driver.get(TestData.BASE_URL)

    def test_login_page_title(self):
        title = self.login_page.get_login_title(LoginLocators.LOGIN_PAGE_TITLE)
        assert title == LoginLocators.LOGIN_PAGE_TITLE

    def go_to_home_page(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        current_url = self.login_page.get_url()
        assert current_url == TestData.HOME_PAGE_URL

    def test_invalid_login(self):
        self.login_page.do_login(TestData.INVALID_USER_NAME, LoginLocators.INVALID_PASSWORD)
        assert self.login_page.is_visible(LoginLocators.ERROR_MESSAGE)
