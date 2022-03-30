from Config.config import Test_Data
from Pages.login_page import Login_Page
from Tests.test_base import Base_Test
from Locators import login_page_locators as locator
from Config import config


class Test_Login(Base_Test):
    def test_signup_link_visible(self):
        self.login_page = Login_Page(self.driver)
        flag = self.login_page.is_signup_link_visible()
        assert flag  # boolian

    def test_login_page_title(self):
        self.login_page = Login_Page(self.login_page)
        title = self.login_page.get_title(Test_Data.LOGIN_PAGE_TITLE)
        assert title == Test_Data.LOGIN_PAGE_TITLE

    def test_login(self):
        self.login_page = Login_Page(self.login_page)
        self.login_page.do_login(Test_Data.USER_NAME, Test_Data.PASSWORD)
        assert self.login_page.get_url() == config.Test_Data.HOME_PAGE_URL

    def test_invalid_login(self):
        self.login_page = Login_Page(self.login_page)
        self.login_page.do_login(Test_Data.INVALID_USER_NAME, Test_Data.PASSWORD)
        assert self.login_page.is_visible(locator.ERROR_MESSAGE)
