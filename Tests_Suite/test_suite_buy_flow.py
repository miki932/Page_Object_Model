from Tests.test_home_page import TestHome
from Tests.test_login_page import TestLogin


class TestBuyingFlow:
    def test_buy_flow(self, init_driver):
        home_page = TestHome(init_driver)
        #home_page.test_twitter_logo()
        home_page.test_facebook_logo()
        # test_home_page.test_linkedin_logo()
        # test_home_page.test_shopping_badge_cart()
