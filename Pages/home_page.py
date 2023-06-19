from Pages.base_page import BasePage
from Locators.home_page_locators import HomePageLocators as homeLocator


class HomePage(BasePage):
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
