from Tests.test_login_page import TestLogin


class TestLoginSanity:
    def test_suite_sanity(self, init_driver):
        test_login = TestLogin(init_driver)
        test_login.test_login_page_title()
        test_login.do_login_and_go_to_home_page()
