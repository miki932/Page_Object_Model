from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Pages.home_page import HomePage
from Locators.home_page_locators import HomePageLocators as homeLocator
from config import TestData


class TestHome(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.home_page = HomePage(self.driver)
        self.driver.get(TestData.HOME_PAGE_URL)

    def test_logo(self, logo, url):
        # Store the ID of the original window
        original_window = self.driver.current_window_handle
        self.home_page.click(logo)
        self.home_page.switch_tab()
        assert self.is_link_work(url)
        self.driver.close()
        self.driver.switch_to.window(original_window)

    def test_shopping_badge_cart(self):
        self.home_page.add_to_cart(homeLocator.ITEM_FOR_SALE_1)
        # print(homeLocator.SHOPPING_CART_BADGE.get_attribute('shopping_cart_badge'))
        # obj = (By.CLASS_NAME, "shopping_cart_badge")
        element = self.driver.find_element(
            By.XPATH,
            '//*[@class="shopping_cart_link"]//*[@class="shopping_cart_badge"]',
        )
        print(element)
        print(type(element))
        # print(element.get_element())

        # assert homeLocator.SHOPPING_CART_BADGE.get_attribute('value') == 1
        # self.home_page.click(homeLocator.BACK_TO_PRODUCT)
        # self.home_page.add_to_cart(homeLocator.ITEM_FOR_SALE_2)
        # assert homeLocator.SHOPPING_CART_BADGE.get_attribute('value') == 2

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
