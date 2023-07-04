from Tests import test_home_page as thp
from Tests import test_login_page as tlp

"This way is more aligned with the recommended pytest practices, but is the same as test_suite_1.py"


def test_twitter_logo(init_driver):
    test_login = tlp.TestLogin()
    test_home = thp.TestHome()
    test_login.test_login(init_driver)
    test_home.test_twitter_logo(init_driver)


def test_facebook_logo(init_driver):
    test_login = tlp.TestLogin()
    test_home = thp.TestHome()
    test_login.test_login(init_driver)
    test_home.test_facebook_logo(init_driver)


def test_cart(init_driver):
    test_login = tlp.TestLogin()
    test_home = thp.TestHome()
    test_login.test_login(init_driver)
    test_home.test_shopping_badge_cart(init_driver)


def test_remove_cart(init_driver):
    test_login = tlp.TestLogin()
    test_home = thp.TestHome()
    test_login.test_login(init_driver)
    test_home.test_remove_from_cart(init_driver)


def test_about(init_driver):
    test_login = tlp.TestLogin()
    test_home = thp.TestHome()
    test_login.test_login(init_driver)
    test_home.test_go_to_about_page(init_driver)


def test_logout(init_driver):
    test_login = tlp.TestLogin()
    test_home = thp.TestHome()
    test_login.test_login(init_driver)
    test_home.test_logout_btn(init_driver)


def test_invalid_login(init_driver):
    test_login = tlp.TestLogin()
    test_login.test_invalid_login(init_driver)
