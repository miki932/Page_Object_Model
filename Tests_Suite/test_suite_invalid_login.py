from Tests.test_login_page import TestLogin


def invalid_login(init_driver):
    test_login = TestLogin(init_driver)
    test_login.test_invalid_login()
