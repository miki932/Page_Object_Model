from Tests.test_home_page import TestHome


class TestBuy:
    def test_buy_flow(self, init_driver):
        test_home_page = TestHome(init_driver)
        test_home_page.do_login_and_go_to_home_page_1()
        test_home_page.test_twitter_logo()
        test_home_page.test_facebook_logo()
        # test_home_page.test_linkedin_logo()
        # test_home_page.test_shopping_badge_cart()
