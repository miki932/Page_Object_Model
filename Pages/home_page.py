from Pages.base_page import Base_Page
from Config.config import Test_Data
from Locators import home_page_locators as home_locator
from selenium.webdriver.support.ui import Select


class Home_Page(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Test_Data.HOME_PAGE_URL)

    def add_to_cart(self, by_locator):
        self.click(by_locator)

    def sort(self, value):
        select = Select(home_locator.SORT_BTN)
        select.select_by_value(value)

    def go_to_cart(self, by_locator):
        self.click(by_locator)
