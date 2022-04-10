from Pages.base_page import BasePage
from Locators.cart_page_locators import CartPageLocators


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(CartPageLocators.CART_PAGE_URL)

    # Page Actions:
    def continue_shopping(self):
        self.click(CartPageLocators.CONTINUE_SHOPPING_BTN)

    def checkout(self):
        self.click(CartPageLocators.CHECKOUT_BTN)

    def remove(self):
        self.click(CartPageLocators.REMOVE_BTN)
