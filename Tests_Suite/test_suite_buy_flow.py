from Tests.test_home_page import TestHome


class BuyingFlow:
    def buy_flow(self, init_driver):
        test_home_page = TestHome(init_driver)
        test_home_page.do_login_and_go_to_home_page()
