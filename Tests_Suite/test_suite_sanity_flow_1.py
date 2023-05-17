from Tests.test_home_page import TestHome


class TestBuy:
    def test_buy_flow(self, init_driver):
        test_home_page = TestHome(init_driver)
        test_home_page.do_login_and_go_to_home_page_1()
        test_home_page.test_twitter_logo()
        test_home_page.test_facebook_logo()
        # test_home_page.test_linkedin_logo()
        # test_home_page.test_shopping_badge_cart()


"""
from Tests import test_home_page


def test_login():
    test_home_page.test


def test_twitter():
    test_home_page.test_twitter_logo()


def test_linkedin_logo():
    test_home_page.test_linkedin_logo()


def test_shopping():
    test_home_page.test_shopping_badge_cart()
"""
