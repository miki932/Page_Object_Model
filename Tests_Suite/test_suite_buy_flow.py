import pytest
from Locators.home_page_locators import HomePageLocators as homeLocator
from Tests.test_home_page import TestHome
from Tests.test_login_page import TestLogin


@pytest.mark.reggression
def test_buy_flow(init_driver):
    login_page = TestLogin()
    # Assert login
    login_page.test_login()

    home_page = TestHome()
    # Verify Twitter logo takes us to twitter
    home_page.test_logo(logo=homeLocator.TWITTER_LOGO, url=homeLocator.TWITTER_URL)
    # Verify Facebook logo takes us to Facebook
    home_page.test_logo(logo=homeLocator.FACEBOOK_LOGO, url=homeLocator.FACEBOOK_URL)
    home_page.test_shopping_badge_cart()
