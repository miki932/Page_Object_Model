import logging
from qaseio.pytest import qase
from Tests import test_home_page as thp
from Tests import test_login_page as tlp


"""
Test suite for the Buy Flow functionality.
This suite includes tests for login, navigation, and various UI functionalities after login.
This way is more aligned with the recommended pytest practices, but is the same as test_suite_1.py
"""


logger = logging.getLogger(__name__)


@qase.id(2)
def test_invalid_login(init_driver):
    """Verify error message for an invalid login attempt"""
    test_login = tlp.TestLogin()
    test_login.test_invalid_login(init_driver)
    logger.info(
        "test_invalid_login - Verify error message for an invalid login attempt"
    )


@qase.id(4)
def test_about(init_driver):
    """Verify navigation to the About page after login"""
    test_login = tlp.TestLogin()
    test_home = thp.TestHome()
    test_login.test_login(init_driver)
    test_home.test_go_to_about_page(init_driver)
    logger.info("test_about - Verify navigation to the About page after login")


@qase.id(5)
def test_logout(init_driver):
    """Verify successful logout after login"""
    test_login = tlp.TestLogin()
    test_home = thp.TestHome()
    test_login.test_login(init_driver)
    test_home.test_logout_btn(init_driver)
    logger.info("test_logout - Verify successful logout after login")


# @pytest.mark.qase_case_id("POM-6")
# def test_twitter_logo(init_driver):
#     """Verify Twitter logo functionality after login"""
#     test_login = tlp.TestLogin()
#     test_home = thp.TestHome()
#     test_login.test_login(init_driver)
#     test_home.test_twitter_logo(init_driver)
#     logger.info("test_twitter_logo - Verify Twitter logo functionality after login")
#
#
# @pytest.mark.qase_case_id("POM-7")
# def test_facebook_logo(init_driver):
#     """Verify Facebook logo functionality after login"""
#     test_login = tlp.TestLogin()
#     test_home = thp.TestHome()
#     test_login.test_login(init_driver)
#     test_home.test_facebook_logo(init_driver)
#     logger.info("test_facebook_logo - Verify Facebook logo functionality after login")
#
#
# @pytest.mark.qase_case_id("POM-8")
# def test_cart(init_driver):
#     """Verify shopping cart functionality after adding an item"""
#     test_login = tlp.TestLogin()
#     test_home = thp.TestHome()
#     test_login.test_login(init_driver)
#     test_home.test_shopping_badge_cart(init_driver)
#     logger.info("test_cart - Verify shopping cart functionality after adding an item")
#
#
# @pytest.mark.qase_case_id("POM-10")
# def test_remove_cart(init_driver):
#     """Verify removing an item from the cart"""
#     test_login = tlp.TestLogin()
#     test_home = thp.TestHome()
#     test_login.test_login(init_driver)
#     test_home.test_remove_from_cart(init_driver)
#     logger.info("test_remove_cart - Verify removing an item from the cart")
