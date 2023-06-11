import pytest
from Locators.home_page_locators import HomePageLocators as homeLocator
from Tests.test_home_page import TestHome
from Tests.test_login_page import TestLogin


@pytest.mark.qase_case_id("CASE_ID")
def test_buy_flow(init_driver):
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
