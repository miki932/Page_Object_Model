from Tests import test_home_page as thp
from Tests import test_login_page as tlp


"This way is more 'Unit test way', in test_suite_2 I show how is the more aligned to be 'pytest' way"


class TestSuiteBuyFlow:
    def setup_method(self):
        self.test_home = thp.TestHome()
        self.test_login = tlp.TestLogin()

    def test_twitter_logo(self, init_driver):
        self.test_login.test_login(init_driver)
        self.test_home.test_twitter_logo(init_driver)

    def test_facebook_logo(self, init_driver):
        self.test_login.test_login(init_driver)
        self.test_home.test_facebook_logo(init_driver)

    def test_cart(self, init_driver):
        self.test_login.test_login(init_driver)
        self.test_home.test_shopping_badge_cart(init_driver)

    def test_remove_cart(self, init_driver):
        self.test_login.test_login(init_driver)
        self.test_home.test_remove_from_cart(init_driver)

    def test_about(self, init_driver):
        self.test_login.test_login(init_driver)
        self.test_home.test_go_to_about_page(init_driver)

    def test_logout(self, init_driver):
        self.test_login.test_login(init_driver)
        self.test_home.test_logout_btn(init_driver)

    def test_invalid_login(self, init_driver):
        self.test_login.test_invalid_login(init_driver)
