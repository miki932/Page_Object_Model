from selenium.webdriver.common.by import By


# Object Repository:

#Header
SHOPPING_CART = (By.ID, 'shopping_cart_container')
SHOPPING_CART_BADGE = (By.ID, '//*[@id="shopping_cart_container"]//*[@class="shopping_cart_link"]//*[@class="shopping_cart_badge"]')
BURGER_MENU = (By.ID, 'react-burger-menu-btn')
SORT_BTN = (By.CLASS_NAME, 'active_option')

ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-backpack')
REMOVE_FROM_CART = (By.ID, 'remove-sauce-labs-backpack')

ITEM_FOR_SALE_1 = (By.XPATH, '//*[@id="inventory_container"]//*[@class="inventory_list"]//*[@class="inventory_item"]//*[@id="item_4_title_link"]')
ITEM_FOR_SALE_2 = (By.XPATH, '//*[@id="inventory_container"]//*[@class="inventory_list"]//*[@class="inventory_item"]//*[@id="item_0_title_link"]')
ITEM_FOR_SALE_3 = (By.XPATH, '//*[@id="inventory_container"]//*[@class="inventory_list"]//*[@class="inventory_item"]//*[@id="item_1_title_link"]')
ITEM_FOR_SALE_4 = (By.XPATH, '//*[@id="inventory_container"]//*[@class="inventory_list"]//*[@class="inventory_item"]//*[@id="item_2_title_link"]')
ITEM_FOR_SALE_5 = (By.XPATH, '//*[@id="inventory_container"]//*[@class="inventory_list"]//*[@class="inventory_item"]//*[@id="item_3_title_link"]')

#Footer
TWITTER_LOGO = (By.XPATH, '//*[@id="page_wrapper"]/footer/ul/li[1]/a')
FACEBOOK_LOGO = (By.XPATH, '//*[@id="page_wrapper"]/footer/ul/li[2]/a')
LINKEDIN_LOGO = (By.XPATH, '//*[@id="page_wrapper"]/footer/ul/li[3]/a')

TWITTER_URL = "https://twitter.com/saucelabs"
FACEBOOK_URL = "https://www.facebook.com/saucelabs"
LINKEDIN_URL = "https://www.linkedin.com/company/sauce-labs/"