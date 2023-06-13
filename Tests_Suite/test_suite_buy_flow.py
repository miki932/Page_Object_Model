import pytest

from Locators.home_page_locators import HomePageLocators as homeLocator
from Tests.test_home_page import TestHome
from Tests.test_login_page import TestLogin


"""
def test_buy_flow(init_driver):
    driver = init_driver
    login_page = TestLogin(init_driver)

    # Assert login
    login_page.test_login()
    home_page = TestHome(init_driver)

    # Verify Twitter logo takes us to Twitter
    home_page.test_logo(logo=homeLocator.TWITTER_LOGO, url=homeLocator.TWITTER_URL)

    # Verify Facebook logo takes us to Facebook
    home_page.test_logo(logo=homeLocator.FACEBOOK_LOGO, url=homeLocator.FACEBOOK_URL)
    home_page.test_shopping_badge_cart()
    home_page.test_remove_from_cart()
    home_page.test_go_to_about_page()
    home_page.test_logout_btn()
@pytest.fixture()
def test_home(request):
    yield TestHome("this is test hime class")
"""


def test_suite_home(test_home):
    # Call the test methods from the TestHome class
    test_home.test_logo(homeLocator.TWITTER_LOGO, homeLocator.TWITTER_URL)


def test_suite_home_2(test_home):
    test_home.test_logo(homeLocator.FACEBOOK_LOGO, homeLocator.FACEBOOK_URL)


def test_suite_home_3(test_home):
    test_home.test_shopping_badge_cart()


def test_suite_home_4(test_home):
    test_home.test_remove_from_cart()


def test_suite_home_5(test_home):

    test_home.test_go_to_about_page()


def test_suite_home_6(test_home):
    test_home.test_logout_btn()
