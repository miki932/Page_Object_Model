from Tests.test_login_page import *
from Locators.login_page_locators import LoginLocators


class TestLoginSanity:
    def test_suite_1(self, init_driver):
        login_page = LoginPage(init_driver)
        login_page.get_login_title(LoginLocators.LOGIN_PAGE_TITLE)
