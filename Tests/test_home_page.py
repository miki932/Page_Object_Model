from Pages.base_page import BasePage
from Pages.home_page import HomePage
from Locators.home_page_locators import HomePageLocators as homeLocator
from Configurations.config import TestData


class TestHome(BasePage):
    def __init__(self, driver, base_url=TestData.HOME_PAGE_URL):
        super().__init__(driver)
        self.driver = driver
        self.base_url = base_url
        self.home_page = HomePage(driver)

    def test_logo(self, logo, url):
        # Store the ID of the original window
        original_window = self.driver.current_window_handle
        self.home_page.click(logo)
        self.home_page.switch_window(1)
        assert self.is_link_work(url)
        self.driver.close()
        self.driver.switch_to.window(original_window)

    def test_shopping_badge_cart(self):
        self.home_page.add_to_cart(homeLocator.ITEM_FOR_SALE_1)
        self.home_page.click(homeLocator.ADD_TO_CART)
        cart_counter = self.home_page.get_element(homeLocator.SHOPPING_CART_BADGE)
        print(f"******{cart_counter}*******")
        assert int(cart_counter) == 1
        assert self.home_page.is_visible(homeLocator.IMAGE_ITEM)

    def test_remove_from_cart(self):
        self.home_page.add_to_cart(homeLocator.ITEM_FOR_SALE_1)
        self.home_page.add_to_cart(homeLocator.ITEM_FOR_SALE_2)
        self.home_page.click(homeLocator.REMOVE_FROM_CART)
        assert homeLocator.SHOPPING_CART_BADGE == 1

    def test_go_to_about_page(self):
        self.home_page.go_to_about_page()
        assert self.home_page.get_url() == homeLocator.ABOUT_PAGE_URL

    def test_logout_btn(self):
        self.home_page.go_to_logout()
        assert self.get_url() == TestData.BASE_URL
