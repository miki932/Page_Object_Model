from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Configurations import config


class CartPage(BasePage):
    # Locators
    CHECKOUT_BTN = (By.ID, "cart")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")
    ITEM_TITLE_LINK = (By.ID, "item_0_title_link")

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = config.CART_PAGE_URL

    # Page Actions:
    def continue_shopping(self):
        self.click(CartPage.CONTINUE_SHOPPING_BTN)

    def checkout(self):
        self.click(CartPage.CHECKOUT_BTN)

    def remove_item(self):
        self.click(CartPage.REMOVE_BTN)

    def get_item_title(self):
        return self.get_element_text(CartPage.ITEM_TITLE_LINK)
