from Pages.base_page import BasePage
from Pages.home_page import HomePage
from Locators.home_page_locators import HomePageLocators as homeLocator
from config import TestData


class TestHome(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.home_page = HomePage(self.driver)
        self.driver.get(TestData.HOME_PAGE_URL)

    def test_twitter_logo(self, url=homeLocator.TWITTER_URL):
        self.home_page.click(homeLocator.TWITTER_LOGO)
        self.home_page.switch_tab()
        assert self.is_link_work(url)
        self.home_page.close_current_tab()


    def test_facebook_logo(self,url=homeLocator.FACEBOOK_URL):
        self.home_page.click(homeLocator.FACEBOOK_LOGO)
        self.home_page.switch_tab()
        assert self.is_link_work(url)

    def test_linkedin_logo(self, url=homeLocator.LINKEDIN_URL):
        self.home_page.click(homeLocator.LINKEDIN_LOGO)
        self.home_page.switch_tab()
        assert self.is_link_work(url)

    def test_shopping_badge_cart(self):
        self.home_page.add_to_cart(homeLocator.ITEM_FOR_SALE_1)
        assert homeLocator.SHOPPING_CART_BADGE == 1
        self.home_page.add_to_cart(homeLocator.ITEM_FOR_SALE_2)
        assert homeLocator.SHOPPING_CART_BADGE == 2

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
        