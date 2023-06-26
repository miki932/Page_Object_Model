from Pages.login_page import LoginPage
from Configurations import config
import pytest


class TestLogin:
    def test_login(self, init_driver):
        login_page = LoginPage(init_driver)
        login_page.do_login(config.USER_NAME, config.PASSWORD)
        current_url = login_page.get_url()
        print(current_url)
        assert current_url == config.HOME_PAGE_URL

    def test_invalid_login(self, init_driver):
        login_page = LoginPage(init_driver)
        login_page.go_to()
        login_page.invalid_login(config.INVALID_USER_NAME, config.INVALID_PASSWORD)
        err_msg = login_page.is_visible(LoginPage.BAD_PASSWORD_OR_USERNAME_ERROR)
        assert err_msg, "Invalid login error message is not displayed"

    def test_login_page_title(self, init_driver):
        login_page = LoginPage(init_driver)
        title = login_page.get_login_title(LoginPage.LOGIN_PAGE_TITLE)
        assert title == LoginPage.LOGIN_PAGE_TITLE
