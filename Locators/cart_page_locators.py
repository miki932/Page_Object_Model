from selenium.webdriver.common.by import By


class Cart_Page_Locators:
    CART_PAGE_URL = "https://www.saucedemo.com/cart.html"
    CHECKOUT_BTN = (By.ID, "cart")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")
