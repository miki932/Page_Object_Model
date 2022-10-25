from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TestData

"""
# TODO: fix driver issue
# TODO: custom logger.
# TODO: get element func.
# TODO: Jenkins integration.
# TODO: TestPlan management integration.
# TODO: Wrap all in Docker.
# TODO: Run test in parallel.
# TODO: Allure integration.
# TODO: Add option from command line (chrome, firefox).
# TODO: Pytest - Separate to regression/sanity etc.
"""


class BasePage:
    """
    The Base_Page class is a parent of all pages & holds all common
    functionality across the website.
    """

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    # Basic actions
    def click(self, locator):
        """Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        ).click()

    def send_text(self, locator, text):
        """Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def get_element_text(self, locator):
        return self.driver.find_element(locator).text

    def hover(self, locator):
        element = self.driver.find_element(locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        try:
            WebDriverWait(self.driver, TestData.TIMEOUT).until(EC.title_is(title))
        except TimeoutException:
            print("ERROR: ELEMENT NOT FOUND WITHIN GIVEN TIME")
        return self.driver.title

    def get_element(self, locator) -> str:

        element = WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    def is_visible(self, locator):
        element = WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )
        return bool(element)

    def get_url(self) -> str:
        return self.driver.current_url

    def is_link_work(self, url):
        url_exists = WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.url_to_be(url)
        )
        return url_exists

    def switch_tab(self):
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.number_of_windows_to_be(2)
        )
        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

    def close_current_tab(self):
        self.driver.close()

    def accept_alert(self, text=""):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        if text in alert_text:
            alert.accept()
        else:
            raise Exception(
                f"Invalid alert with text {alert_text} and not containing {text}"
            )
        return alert_text

    def dismiss_alert(self, text):
        alert = self.driver.switch_to.alert()
        alert_text = alert.text
        if text in alert_text:
            alert.dismiss()
        else:
            raise Exception(
                f"Invalid alert with text {alert_text} and not containing {text}"
            )
        return alert_text

    def focus(self):
        another_window = list(
            set(self.driver.window_handles) - {self.driver.current_window_handle}
        )[0]
        self.driver.switch_to.window(another_window)

    def print_current_url(self):
        get_url = self.driver.current_url
        print("The current url is:" + str(get_url))


"""
    def check_element_displayed(self, locator):
        # This method checks if the web element is present in page or not and returns True or False accordingly

        result_flag = False
        try:
            if self.get_element(locator) is not None:
                element = self.get_element(locator, verbose_flag=False)
                if element.is_displayed() is True:
                    result_flag = True
        except Exception as e:
            self.write(e)
            self.exceptions.append(
                "Web element not present in the page, please check the"
                f" locator is correct - {locator} in the conf/locators.conf file"
            )

        return result_flag

    def check_element_present(self, locator):
        # This method checks if the web element is present in page or not and returns True or False accordingly
        result_flag = False
        if self.get_element(locator, verbose_flag=False) is not None:
            result_flag = True

        return result_flag

    def find_element_in_page(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
        
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
    
        return True
        
    def get_text(self, locator="", locator_type="id", element=None, info=""):
            
            Get the 'Text' displayed for an element
            Either provide element or a combination of locator and locator_type
            :param locator: Unique identifier for the element to be found
            :param locator_type: Type of locator being passed (default "id")
            :param element: Element to perform the action against
            :param info: Message to be included in the logs        
            
            try:
                # if locator passed in, go find the associated element
                if locator:
                    element = self.get_element(locator, locator_type)
                text = element.text
                self.log.debug("Found element size: " + str(len(text)))
                if len(text) == 0:
                    text = element.get_attribute("innerText")
                if len(text) != 0:
                    self.log.debug("Getting text on element: " + info)
                    self.log.debug("The text is: " + text)
                    text = text.strip()
            except:
                self.log.error("Failed to get text on element: " + info)
                print_stack()
                text = None
            return text
            
        import csv
    def getCSVData(fileName):
        # create an empty list to store rows
        rows = []
        # open the CSV file
        dataFile = open(fileName, "r")
        # create a CSV Reader from CSV file
        reader = csv.reader(dataFile)
        # skip the headers
        next(reader)
        # add rows from reader to list
        for row in reader:
            rows.append(row)
        return rows
        

    def verify_title(self):
        if self.get_title() == 'Google':
            return True
        else:
            return False
            
    
import logging

class LogGen:

    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(filename="./Logs/automation.log", filemode='w',
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


        
import inspect
import logging


def customLogger(logLevel=logging.DEBUG):

# Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
# By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(logLevel)

# Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M:%S %p')

# add formatter to console handler --> chandler
    fileHandler.setFormatter(formatter)

# add console handler to logger
    logger.addHandler(fileHandler)

    return logger
    
    
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
"""
