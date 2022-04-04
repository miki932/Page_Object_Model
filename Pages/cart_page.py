from Pages.base_page import Base_Page
from Locators.cart_page_locators import Cart_Page_Locators


class Cart_Page(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Cart_Page_Locators.CART_PAGE_URL)

    def continue_shopping(self):
        self.click(Cart_Page_Locators.CONTINUE_SHOPPING_BTN)

    def checkout(self):
        self.click(Cart_Page_Locators.CHECKOUT_BTN)

    def get_items(self):
        pass

    def remove(self, item):
        pass
