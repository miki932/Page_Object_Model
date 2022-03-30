from Tests.test_base import Base_Test
from Pages.home_page import Home_Page
from Locators import home_page_locators as home_locator


class Test_Home(Base_Test):

    def test_twitter_logo(self):
        self.home_page = Home_Page(self.driver)
        self.home_page.click(home_locator.TWITTER_LOGO)
        assert self.home_page.get_url() == home_locator.TWITTER_URL

    def test_facebook_logo(self):
        self.home_page = Home_Page(self.driver)
        self.home_page.click(home_locator.FACEBOOK_LOGO)
        assert self.home_page.get_url() == home_locator.FACEBOOK_URL

    def test_linkedin_logo(self):
        self.home_page = Home_Page(self.driver)
        self.home_page.click(home_locator.LINKEDIN_LOGO)
        assert self.home_page.get_url() == home_locator.LINKEDIN_URL

    def test_shopping_badge_cart(self):
        self.home_page = Home_Page(self.driver)
        self.home_page.add_to_cart(home_locator.ITEM_FOR_SALE_1)
        assert home_locator.SHOPPING_CART_BADGE == 1
        self.home_page.add_to_cart(home_locator.ITEM_FOR_SALE_2)
        assert home_locator.SHOPPING_CART_BADGE == 2

    def test_remove_from_cart(self):
        self.home_page = Home_Page(self.driver)
        self.home_page.add_to_cart(home_locator.ITEM_FOR_SALE_1)
        self.home_page.add_to_cart(home_locator.ITEM_FOR_SALE_2)
        self.home_page.click(home_locator.REMOVE_FROM_CART)
        assert home_locator.SHOPPING_CART_BADGE == 1

    def test_go_to_about_page(self):
        self.home_page.go_to_about_page()
        assert self.home_page.get_url() == home_locator.HOME_PAGE_URL