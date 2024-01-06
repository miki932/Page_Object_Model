import pytest
from Tests import test_home_page as thp
from Tests import test_login_page as tlp
from logger import logger


class TestSuiteBuyFlow:
    def setup_method(self):
        """Setting up the test suite."""
        self.test_home = thp.TestHome()
        self.test_login = tlp.TestLogin()
        logger.info("setup_method - Setting up the test suite")

    @pytest.mark.qase("POM-1")
    def test_login(self, init_driver):
        """Verify successful login."""
        self.test_login.test_login(init_driver)
        logger.info("test_login - Verify successful login")

    @pytest.mark.qase("POM-2")
    def test_invalid_login(self, init_driver):
        """Verify error message for invalid login attempt."""
        self.test_login.test_invalid_login(init_driver)
        logger.info(
            "test_invalid_login - Verify error message for invalid login attempt"
        )

    @pytest.mark.qase("POM-3")
    def test_title(self, init_driver):
        """Title verification after login completed."""
        self.test_login.test_login(init_driver)
        self.test_login.test_login_page_title(init_driver)
        logger.info("test_title - Title verification after login completed")

    @pytest.mark.qase("POM-4")
    def test_about(self, init_driver):
        """Verify navigation to the About page after login."""
        self.test_login.test_login(init_driver)
        self.test_home.test_go_to_about_page(init_driver)
        logger.info("test_about - Verify navigation to the About page after login")

    @pytest.mark.qase("POM-5")
    def test_logout(self, init_driver):
        """Verify successful logout after login."""
        self.test_login.test_login(init_driver)
        self.test_home.test_logout_btn(init_driver)
        logger.info("test_logout - Verify successful logout after login")

    @pytest.mark.qase("POM-6")
    def test_twitter_logo(self, init_driver):
        """Verify Twitter logo functionality after login."""
        self.test_login.test_login(init_driver)
        self.test_home.test_twitter_logo(init_driver)
        logger.info("test_twitter_logo - Verify Twitter logo functionality after login")

    @pytest.mark.qase("POM-7")
    def test_facebook_logo(self, init_driver):
        """Verify Facebook logo functionality after login."""
        self.test_login.test_login(init_driver)
        self.test_home.test_facebook_logo(init_driver)
        logger.info(
            "test_facebook_logo - Verify Facebook logo functionality after login"
        )

    @pytest.mark.qase("POM-8")
    def test_badge_cart(self, init_driver):
        """Verify shopping cart badge after adding an item."""
        self.test_login.test_login(init_driver)
        self.test_home.test_shopping_badge_cart(init_driver)
        logger.info("test_badge_cart - Verify shopping cart badge after adding an item")

    @pytest.mark.qase("POM-10")
    def test_remove_cart(self, init_driver):
        """Verify removing an item from the cart."""
        self.test_login.test_login(init_driver)
        self.test_home.test_remove_from_cart(init_driver)
        logger.info("test_remove_cart - Verify removing an item from the cart")
