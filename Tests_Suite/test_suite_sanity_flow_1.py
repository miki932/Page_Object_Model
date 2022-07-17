
from Tests.test_home_page import TestHome


class TestBuy:
    def test_buy(self, init_driver):
        test_home_page = TestHome(init_driver)
        test_home_page.do_login_and_go_to_home_page_1()
