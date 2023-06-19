import pytest
from Locators.home_page_locators import HomePageLocators as homeLocator
from Tests.test_home_page import TestHome
from Tests.test_login_page import TestLogin


@pytest.mark.usefixtures("init_driver")
class TestSuiteBuyFlow:
    def test_suite_home(self):
        test_home = TestHome()
        test_login = TestLogin()
        test_login.test_login()
        # Call the test methods from the TestHome class
        test_home.test_logo(homeLocator.TWITTER_LOGO, homeLocator.TWITTER_URL)

    def test_suite_home_2(self):
        test_home = TestHome()
        test_login = TestLogin()
        test_login.test_login()
        test_home.test_logo(homeLocator.FACEBOOK_LOGO, homeLocator.FACEBOOK_URL)

    def test_suite_home_3(self):
        test_home = TestHome()
        test_login = TestLogin()
        test_login.test_login()
        test_home.test_shopping_badge_cart()

    def test_suite_home_4(self):
        test_home = TestHome()
        test_login = TestLogin()
        test_login.test_login()
        test_home.test_remove_from_cart()

    def test_suite_home_5(self):
        test_home = TestHome()
        test_login = TestLogin()
        test_login.test_login()
        test_home.test_go_to_about_page()

    def test_suite_home_6(self):
        test_home = TestHome()
        test_login = TestLogin()
        test_login.test_login()
        test_home.test_logout_btn()
