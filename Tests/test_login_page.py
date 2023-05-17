from Pages.base_page import BasePage
from Pages.login_page import LoginPage
from Locators.login_page_locators import LoginLocators
from Configurations import config


class TestLogin(BasePage):
    # def __init__(self, driver, base_url=TestData.BASE_URL):
    # super().__init__(driver)
    # self.driver = driver
    # self.base_url = base_url
    # self.login_page = LoginPage(driver)
    def test_login(self):
        self.login_page.do_login(config.USER_NAME, config.PASSWORD)
        current_url = self.login_page.get_url()
        assert current_url == config.HOME_PAGE_URL

    def test_invalid_login(self):
        self.login_page.invalid_login(config.INVALID_USER_NAME, config.INVALID_PASSWORD)
        err_msg = self.login_page.is_visible(
            LoginLocators.BAD_PASSWORD_OR_USERNAME_ERROR
        )
        assert err_msg

    def test_login_page_title(self):
        title = self.login_page.get_login_title(LoginLocators.LOGIN_PAGE_TITLE)
        assert title == LoginLocators.LOGIN_PAGE_TITLE
