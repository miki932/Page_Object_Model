from Tests.test_login_page import Test_Login

def test_suite_1(init_driver):
    Test_Login.test_invalid_login()