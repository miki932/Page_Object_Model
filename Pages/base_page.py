from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory.Pagefactory import PageFactory
from Config.config import TestData


class BasePage(PageFactory):
    """
    The Base_Page class is a parent of all pages & holds all common functionality across the website.
    Also provides a nice wrapper when dealing with selenium functions that may
    not be easy to understand.
    I'm inherit from `selenium-page-factory.PageFactory` which is a simple Python library
    that provides page factory approach to implement page object model in selenium.
    """
    def __init__(self, driver):
        """This function is called every time a new object of the base class that created"""
        super().__init__()
        self.driver = driver

    def click(self, by_locator):
        """Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.visibility_of_element_located(by_locator)
        ).click()

    def send_text(self, by_locator, text):
        """Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.visibility_of_element_located(by_locator)
        ).send_keys(text)

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.title_is(title))
        return self.driver.title

    def get_element(self, by_locator) -> str:
        element = WebDriverWait(self, TestData.TIMEOUT).until(
            EC.visibility_of_element_located(by_locator)
        )
        return element.text

    def is_visible(self, by_locator) -> bool:
        element = WebDriverWait(self, TestData.TIMEOUT).until(
            EC.visibility_of_element_located(by_locator)
        )
        return bool(element)

    def get_url(self) -> str:
        return self.driver.current_url()
