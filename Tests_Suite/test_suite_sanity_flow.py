from Tests.test_login_page import TestLogin
from Locators.login_page_locators import LoginLocators
from Config.config import TestData


class TestLoginSanity:
    def test_suite_1(self, init_driver):
        test_login = TestLogin(init_driver)
        test_login.test_login_page_title()
        test_login.go_to_home_page()

#test_login.do_login(TestData.USER_NAME, TestData.PASSWORD)
