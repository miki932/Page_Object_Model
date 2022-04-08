from Tests.test_login_page import Test_Login


def test_suite_1(init_driver):
    Test_Login.test_login_page_title()
    Test_Login.go_to_home_page()
