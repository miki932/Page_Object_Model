from Pages.home_page import HomePage
from Configurations import config


class TestHome:
    def test_twitter_logo(self, init_driver):
        """Test that clicking the Twitter logo - opens a new window & the link works"""
        home_page = HomePage(init_driver)
        original_window = home_page.get_current_window_handle()
        home_page.click(HomePage.TWITTER_LOGO)
        home_page.switch_window(1)
        assert home_page.is_link_work(HomePage.TWITTER_URL)
        home_page.close_current_tab()
        home_page.switch_window(original_window)

    def test_facebook_logo(self, init_driver):
        """Test that clicking the Facebook logo - opens a new window & the link works"""
        home_page = HomePage(init_driver)
        original_window = home_page.get_current_window_handle()
        home_page.click(HomePage.FACEBOOK_LOGO)
        home_page.switch_window(1)
        assert home_page.is_link_work(HomePage.FACEBOOK_URL)
        home_page.close_current_tab()
        home_page.switch_window(original_window)

    def test_shopping_badge_cart(self, init_driver):
        """Test adding an item to the cart & verifying the shopping cart badge"""
        home_page = HomePage(init_driver)
        home_page.click(HomePage.TITLE_OF_ITEM_1)
        home_page.click(HomePage.ADD_TO_CART)
        cart_counter = home_page.get_element(HomePage.SHOPPING_CART_BADGE)
        assert int(cart_counter) == 1
        assert home_page.is_visible(HomePage.IMAGE_ITEM)

    def test_remove_from_cart(self, init_driver):
        """Test removing an item from the cart & verifying the shopping cart badge"""
        home_page = HomePage(init_driver)
        home_page.click(HomePage.BUTTON_ADD_TO_CART_ITEM_1)
        home_page.click(HomePage.BUTTON_ADD_TO_CART_ITEM_2)
        home_page.click(HomePage.REMOVE_FROM_CART)
        cart_counter = home_page.get_element(HomePage.SHOPPING_CART_BADGE)
        assert int(cart_counter) == 1

    def test_go_to_about_page(self, init_driver):
        """Test navigating to the About page & verifying the URL"""
        home_page = HomePage(init_driver)
        home_page.go_to_about_page()
        assert home_page.get_url() == HomePage.ABOUT_PAGE_URL

    def test_logout_btn(self, init_driver):
        """Test clicking the Logout button & verifying the URL"""
        home_page = HomePage(init_driver)
        home_page.go_to_logout()
        assert home_page.get_url() == config.BASE_URL
