from Config.config import Test_Data
from Pages.login_page import Login_Page
from Tests.test_base import Base_Test
from Locators.login_page_locators import Login_Locators
from Config.config import Test_Data


class Test_Login(Base_Test):

    def __init__(self):
        self.login_page = Login_Page(self.driver)

    def test_signup_link_visible(self):
        flag = self.login_page.is_signup_link_visible()
        assert flag  # boolean

    def test_login_page_title(self):
        title = self.login_page.get_title()
        assert title == Test_Data.LOGIN_PAGE_TITLE

    def go_to_home_page(self):
        self.login_page.do_login(Test_Data.USER_NAME, Test_Data.PASSWORD)
        assert self.login_page.get_url() == Test_Data.HOME_PAGE_URL

    def test_invalid_login(self):
        self.login_page.do_login(Test_Data.INVALID_USER_NAME, Login_Locators.INVALID_PASSWORD)
        assert self.login_page.is_visible(Login_Locators.ERROR_MESSAGE)
