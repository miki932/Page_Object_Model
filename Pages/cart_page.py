from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Configurations import config


class CartPage(BasePage):
    """
    This class represents the cart page of the website.
    """

    CHECKOUT_BTN = (By.ID, "cart")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")
    ITEM_TITLE_LINK = (By.ID, "item_0_title_link")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = config.CART_PAGE_URL

    def continue_shopping(self):
        """
        Click on the continue shopping button.
        """
        self.click(CartPage.CONTINUE_SHOPPING_BTN)

    def checkout(self):
        """
        Click on the checkout button.
        """
        self.click(CartPage.CHECKOUT_BTN)

    def remove_item(self):
        """
        Click on the remove item button.
        """
        self.click(CartPage.REMOVE_BTN)

    def get_item_title(self):
        """
        Returns the text of the item title link.
        """
        return self.get_element_text(CartPage.ITEM_TITLE_LINK)
