from Tests.test_base import BaseTest
from Pages.home_page import HomePage
from Locators.home_page_locators import HomePageLocators as homeLocator
from Config.config import TestData


class TestHome(BaseTest):

    def __init__(self):
        self.home_page = HomePage(self.driver)

    def test_twitter_logo(self):
        self.home_page.click()
        assert self.home_page.get_url() == homeLocator.TWITTER_URL

    def test_facebook_logo(self):
        self.home_page.click(homeLocator.FACEBOOK_LOGO)
        assert self.home_page.get_url() == homeLocator.FACEBOOK_URL

    def test_linkedin_logo(self):
        self.home_page.click(homeLocator.LINKEDIN_LOGO)
        assert self.home_page.get_url() == homeLocator.LINKEDIN_URL

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
        