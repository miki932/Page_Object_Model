from Configurations import config
from Pages.base_page import BasePage
from Locators.home_page_locators import HomePageLocators as homeLocator


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(config.HOME_PAGE_URL)

    # Page Actions:
    def add_to_cart(self, by_locator):
        self.click(by_locator)

    def go_to_cart(self, by_locator):
        self.click(by_locator)

    def go_to_about_page(self):
        self.click(homeLocator.BURGER_MENU)
        self.click(homeLocator.ABOUT_PAGE)

    def go_to_logout(self):
        self.click(homeLocator.BURGER_MENU)
        self.click(homeLocator.LOGOUT_BTN)
