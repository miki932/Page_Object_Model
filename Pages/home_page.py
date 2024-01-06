from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class HomePage(BasePage):
    # Locators:
    SHOPPING_CART = (By.ID, "shopping_cart_container")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    SORT_BTN = (By.CLASS_NAME, "active_option")
    BACK_TO_PRODUCT = (By.ID, "back-to-products")
    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_FROM_CART = (By.ID, "remove-sauce-labs-backpack")
    IMAGE_ITEM = (By.CLASS_NAME, "inventory_details_img_container")

    BUTTON_ADD_TO_CART_ITEM_1 = (
        By.XPATH,
        "//button[@id='add-to-cart-sauce-labs-backpack']",
    )
    BUTTON_ADD_TO_CART_ITEM_2 = (
        By.XPATH,
        "//button[@id='add-to-cart-sauce-labs-bike-light']",
    )

    TITLE_OF_ITEM_1 = (
        By.CSS_SELECTOR,
        "a[id='item_4_title_link'] div[class='inventory_item_name']",
    )

    # Footer
    TWITTER_LOGO = (
        By.XPATH,
        '//*[@class="footer"]//*[@class="social"]//*[@class="social_twitter"]',
    )
    FACEBOOK_LOGO = (
        By.XPATH,
        '//*[@class="footer"]//*[@class="social"]//*[@class="social_facebook"]',
    )
    # URL
    TWITTER_URL = "https://twitter.com/i/flow/login?redirect_after_login=%2Fsaucelabs"
    FACEBOOK_URL = "https://www.facebook.com/saucelabs"
    CART_PAGE_URL = "https://www.saucedemo.com/cart.html"

    # Burger Button
    ABOUT_PAGE = (By.ID, "about_sidebar_link")
    ABOUT_PAGE_URL = "https://saucelabs.com/"
    LOGOUT_BTN = (By.ID, "logout_sidebar_link")

    # Page Actions:
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_about_page(self):
        self.click(HomePage.BURGER_MENU)
        self.click(HomePage.ABOUT_PAGE)

    def go_to_logout(self):
        self.click(HomePage.BURGER_MENU)
        self.click(HomePage.LOGOUT_BTN)
