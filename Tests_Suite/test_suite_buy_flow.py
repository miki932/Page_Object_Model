from Tests.test_home_page import TestHome
from Tests.test_login_page import TestLogin
from Locators.home_page_locators import HomePageLocators as homeLocator

#class TestBuyingFlow:
def test_buy_flow(init_driver):
    login_page = TestLogin(init_driver)
    login_page.test_login()
    home_page = TestHome(init_driver)
    home_page.test_twitter_logo()
    home_page.test_facebook_logo()
    #home_page.test_linkedin_logo()
    #home_page.test_shopping_badge_cart()
