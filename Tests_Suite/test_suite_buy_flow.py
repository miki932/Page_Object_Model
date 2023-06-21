from Pages.home_page import HomePage
from Tests.test_home_page import TestHome
from Tests.test_login_page import TestLogin


class TestSuiteBuyFlow:
    def setup(self):
        self.test_home = TestHome()
        self.test_login = TestLogin()

    def test_suite_home(self, init_driver):
        self.test_login.test_login(init_driver)
        self.test_home.test_twitter_logo(init_driver)

    def test_suite_home_2(self, init_driver):
        self.test_login.test_login(init_driver)
        self.test_home.test_facebook_logo(init_driver)

    def test_suite_home_3(self, init_driver):
        self.test_login.test_login(init_driver)
        self.test_home.test_shopping_badge_cart(init_driver)

    def test_suite_home_4(self, init_driver):
        self.test_login.test_login(init_driver)
        self.test_home.test_remove_from_cart(init_driver)

    def test_suite_home_5(self, init_driver):
        self.test_login.test_login(init_driver)
        self.test_home.test_go_to_about_page(init_driver)

    def test_suite_home_6(self, init_driver):
        self.test_login.test_login(init_driver)
        self.test_home.test_logout_btn(init_driver)
