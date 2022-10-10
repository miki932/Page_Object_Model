from selenium.webdriver.common.by import By


class HomePageLocators:
    # Object Repository:
    SHOPPING_CART = (By.ID, "shopping_cart_container")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    SORT_BTN = (By.CLASS_NAME, "active_option")
    BACK_TO_PRODUCT = (By.ID, "back-to-products")
    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_FROM_CART = (By.ID, "remove-sauce-labs-backpack")

    ITEM_FOR_SALE_1 = (
        By.XPATH,
        '//*[@id="inventory_container"]//*[@class="inventory_list"]//*[@class="inventory_item"]//*[@id="item_4_title_link"]',
    )
    ITEM_FOR_SALE_2 = (
        By.XPATH,
        '//*[@id="inventory_container"]//*[@class="inventory_list"]//*[@class="inventory_item"]//*[@id="item_0_title_link"]',
    )
    ITEM_FOR_SALE_3 = (
        By.XPATH,
        '//*[@id="inventory_container"]//*[@class="inventory_list"]//*[@class="inventory_item"]//*[@id="item_1_title_link"]',
    )
    ITEM_FOR_SALE_4 = (
        By.XPATH,
        '//*[@id="inventory_container"]//*[@class="inventory_list"]//*[@class="inventory_item"]//*[@id="item_2_title_link"]',
    )
    ITEM_FOR_SALE_5 = (
        By.XPATH,
        '//*[@id="inventory_container"]//*[@class="inventory_list"]//*[@class="inventory_item"]//*[@id="item_3_title_link"]',
    )

    # Footer
    TWITTER_LOGO = (By.XPATH, '//*[@id="page_wrapper"]/footer/ul/li[1]/a')
    FACEBOOK_LOGO = (By.XPATH, '//*[@id="page_wrapper"]/footer/ul/li[2]/a')

    TWITTER_URL = "https://twitter.com/saucelabs"
    FACEBOOK_URL = "https://www.facebook.com/saucelabs"
    CART_PAGE_URL = "https://www.saucedemo.com/cart.html"

    # Burger Button
    ABOUT_PAGE = (By.ID, "about_sidebar_link")
    ABOUT_PAGE_URL = "https://saucelabs.com/"
    LOGOUT_BTN = (By.ID, "logout_sidebar_link")
