from Pages.base_page import BasePage
from Locators.cart_page_locators import CartPageLocators


class CartPage(BasePage):
    # Page Actions:
    def continue_shopping(self):
        self.click(CartPageLocators.CONTINUE_SHOPPING_BTN)

    def checkout(self):
        self.click(CartPageLocators.CHECKOUT_BTN)

    def remove(self):
        self.click(CartPageLocators.REMOVE_BTN)
