from Tests.test_base import Base_Test
from Pages.home_page import Home_Page
from Locators.home_page_locators import Home_Page_Locators as home_locator
from Config.config import Test_Data

class Test_Home(Base_Test):

    def __init__(self):
        self.home_page = Home_Page(self.driver)

    def test_twitter_logo(self):
        self.home_page.click()
        assert self.home_page.get_url() == home_locator.TWITTER_URL

    def test_facebook_logo(self):
        self.home_page.click(home_locator.FACEBOOK_LOGO)
        assert self.home_page.get_url() == home_locator.FACEBOOK_URL

    def test_linkedin_logo(self):
        self.home_page.click(home_locator.LINKEDIN_LOGO)
        assert self.home_page.get_url() == home_locator.LINKEDIN_URL

    def test_shopping_badge_cart(self):
        self.home_page.add_to_cart(home_locator.ITEM_FOR_SALE_1)
        assert home_locator.SHOPPING_CART_BADGE == 1
        self.home_page.add_to_cart(home_locator.ITEM_FOR_SALE_2)
        assert home_locator.SHOPPING_CART_BADGE == 2

    def test_remove_from_cart(self):
        self.home_page.add_to_cart(home_locator.ITEM_FOR_SALE_1)
        self.home_page.add_to_cart(home_locator.ITEM_FOR_SALE_2)
        self.home_page.click(home_locator.REMOVE_FROM_CART)
        assert home_locator.SHOPPING_CART_BADGE == 1

    def test_go_to_about_page(self):
        self.home_page.go_to_about_page()
        assert self.home_page.get_url() == home_locator.ABOUT_PAGE_URL

    def test_logout_btn(self):
        self.home_page.go_to_logout()
        assert self.get_url() == Test_Data.BASE_URL