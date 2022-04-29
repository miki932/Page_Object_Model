from Tests.test_login_page import TestLogin


class TestInvalidLogin:
    def invalid_login(self, init_driver):
        test_login = TestLogin(init_driver)
        test_login.test_invalid_login()