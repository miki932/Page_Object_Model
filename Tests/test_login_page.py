from Pages.login_page import LoginPage
from Tests.test_base import BaseTest
from Locators.login_page_locators import LoginLocators
from Config.config import TestData


class Test_Login(BaseTest):
    def __init__(self):
        self.login_page = LoginPage(self.driver)
        self.driver.get(TestData.BASE_URL)

    def test_signup_link_visible(self):
        flag = self.login_page.is_signup_link_visible()
        assert flag  # boolean

    def test_login_page_title(self):
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_title(self)
        assert title == LoginLocators.LOGIN_PAGE_TITLE

    def go_to_home_page(self) -> object:
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        assert self.login_page.get_url() == TestData.HOME_PAGE_URL

    def test_invalid_login(self):
        self.login_page.do_login(TestData.INVALID_USER_NAME, LoginLocators.INVALID_PASSWORD)
        assert self.login_page.is_visible(LoginLocators.ERROR_MESSAGE)
