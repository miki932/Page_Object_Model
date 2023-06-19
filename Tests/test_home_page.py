from Pages.home_page import HomePage
from Locators.home_page_locators import HomePageLocators as homeLocator
from Configurations import config


class TestHome:
    def test_logo(self, init_driver, logo, url):
        home_page = HomePage(init_driver)
        original_window = home_page.get_current_window_handle()
        home_page.click(logo)
        home_page.switch_to_window(1)
        assert home_page.is_link_work(url)
        home_page.close_current_window()
        home_page.switch_to_window(original_window)

    def test_shopping_badge_cart(self, init_driver):
        home_page = HomePage(init_driver)
        home_page.add_to_cart(homeLocator.ITEM_FOR_SALE_1)
        home_page.click(homeLocator.ADD_TO_CART)
        cart_counter = home_page.get_element(homeLocator.SHOPPING_CART_BADGE)
        assert int(cart_counter) == 1
        assert home_page.is_visible(homeLocator.IMAGE_ITEM)

    def test_remove_from_cart(self, init_driver):
        home_page = HomePage(init_driver)
        home_page.add_to_cart(homeLocator.ITEM_FOR_SALE_1)
        home_page.add_to_cart(homeLocator.ITEM_FOR_SALE_2)
        home_page.click(homeLocator.REMOVE_FROM_CART)
        cart_counter = home_page.get_element(homeLocator.SHOPPING_CART_BADGE)
        assert int(cart_counter) == 1

    def test_go_to_about_page(self, init_driver):
        home_page = HomePage(init_driver)
        home_page.go_to_about_page()
        assert home_page.get_url() == homeLocator.ABOUT_PAGE_URL

    def test_logout_btn(self, init_driver):
        home_page = HomePage(init_driver)
        home_page.go_to_logout()
        assert home_page.get_url() == config.BASE_URL
