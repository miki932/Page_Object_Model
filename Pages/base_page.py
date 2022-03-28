from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumpagefactory.Pagefactory import PageFactory

class Base_Page(PageFactory):
    """
    The Base_Page class is a parent of all pages & holds all common functionality across the website.
    Also provides a nice wrapper when dealing with selenium functions that may
    not be easy to understand.
    I'm inherit from `selenium-page-factory.PageFactory` which is a simple Python library
    that provides page factory approach to implement page object model in selenium.
    """
    def __init__(self, driver):
        """ This function is called every time a new object of the base class is created"""
        self.driver = driver

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id(self.locator))
        driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id(self.locator))
        element = driver.find_element_by_id(self.locator)
        return element.get_attribute("value")

    def click(self, by_locator):
        """ Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def send_text(self, by_locator, text):
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_element(self, by_locator) -> str:
        element = WebDriverWait(self, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_url(self):
        return self.driver.current_url()