from Locators.home_page_locators import HomePageLocators as homeLocator
from Tests.test_home_page import TestHome
from Tests.test_login_page import TestLogin


def test_suite_home(init_driver):
    test_home = TestHome()
    test_login = TestLogin()
    test_login.test_login(init_driver)
    # Call the test methods from the TestHome class
    test_home.test_logo(init_driver, homeLocator.TWITTER_LOGO, homeLocator.TWITTER_URL)


def test_suite_home_2(init_driver):
    test_home = TestHome()
    test_login = TestLogin()
    test_login.test_login(init_driver)
    test_home.test_logo(
        init_driver, homeLocator.FACEBOOK_LOGO, homeLocator.FACEBOOK_URL
    )


def test_suite_home_3(init_driver):
    test_home = TestHome()
    test_login = TestLogin()
    test_login.test_login(init_driver)
    test_home.test_shopping_badge_cart(init_driver)


def test_suite_home_4(init_driver):
    test_home = TestHome()
    test_login = TestLogin()
    test_login.test_login(init_driver)
    test_home.test_remove_from_cart(init_driver)


def test_suite_home_5(init_driver):
    test_home = TestHome()
    test_login = TestLogin()
    test_login.test_login(init_driver)
    test_home.test_go_to_about_page(init_driver)


def test_suite_home_6(init_driver):
    test_home = TestHome()
    test_login = TestLogin()
    test_login.test_login(init_driver)
    test_home.test_logout_btn(init_driver)
