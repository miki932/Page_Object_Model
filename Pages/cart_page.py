from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class CartPage(BasePage):

    # Locators
    CHECKOUT_BTN = (By.ID, "cart")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")
    ITEM_0_TITLE_LINK = (
        By.ID,
        '//*[@class="cart_list"]//*[@class="cart_item"]'
        '//*[@class="cart_item_label"]//*[@id="item_0_title_link"]',
    )
    CART_PAGE_URL = "https://www.saucedemo.com/cart.html"

    # Page Actions:
    def __init__(self, driver):
        super().__init__(driver)

    def continue_shopping(self):
        self.click(CartPage.CONTINUE_SHOPPING_BTN)

    def checkout(self):
        self.click(CartPage.CHECKOUT_BTN)

    def remove(self):
        self.click(CartPage.REMOVE_BTN)
