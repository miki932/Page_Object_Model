from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TestData
import logging


class BasePage:
    """
    The Base_Page class is a parent of all pages & holds all common
    functionality across the website.

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

    def __init__(self, driver):
        self.driver = driver
        self.highlight_flag = False

    # Basic actions
    def get_element(self, locator):
        WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )
        element = self.driver.find_element(*locator)
        return element

    def click(self, locator):
        """Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def send_text(self, locator, text):
        """Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def hover(self, locator):
        element = self.driver.find_element(locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def execute_script(self, script):
        """
        Execute JavaScript using web driver on selected web element
        :param: Javascript to be execute
        :return: None / depends on Script
        """
        return self.parent.execute_script(script, self)

    def highlight_web_element(self, element):
        """
        To highlight webElement
        :param: WebElement
        :return: None
        """
        if self.highlight:
            self.driver.execute_script(
                "arguments[0].style.border='2px ridge #33ffff'", element
            )

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        try:
            WebDriverWait(self.driver, TestData.TIMEOUT).until(EC.title_is(title))
        except TimeoutException:
            print("ERROR: ELEMENT NOT FOUND WITHIN GIVEN TIME")
        return self.driver.title

    def is_visible(self, locator) -> bool:
        element = WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )
        return bool(element)

    def get_url(self) -> str:
        return self.driver.current_url

    def get_element_attr(self):
        pass

    def is_link_work(self, url):
        url_exists = WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.url_to_be(url)
        )
        return url_exists

    def switch_tab(self):
        """
        I`m Not using this function anymore,
        Because the function `switch_window` (belows) is a better approach from my point of view,
        Because I can handle whatever specific window I want (index), but both are ok and work well.
        """
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.number_of_windows_to_be(2)
        )
        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

    def switch_window(self, index):
        try:
            self.driver.switch_to.window(self.driver.window_handles[index])
        except Exception as e:
            print("Error when switching browser window")
            print(e)

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

    def is_disappeared(self, locator, timeout=TestData.TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout, 1, TestData.TIMEOUT).until_not(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            return False
        return True

    def execute_javascript(self, js_script, *args):
        """Execute JavaScript"""
        try:
            self.driver.execute_script(js_script)
        except Exception as e:
            print(e)

    def turn_on_highlight(self):
        """Highlight the elements being operated upon"""
        self.highlight_flag = True

    def turn_off_highlight(self):
        """Turn off the highlighting feature"""
        self.highlight_flag = False


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
           
    markers =
        regression:
        sanity: 
    
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
        
    def select_drop_down(self, by_locator, text):
        select = Select(self.driver.find_element(*by_locator))
        select.select_by_visible_text(text)
        
    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, 1).until(ec.presence_of_element_located(by_locator)).text

    def switch_alert(self):
        try:
            alert = self.driver.switch_to.alert
        except Exception as e:
            self.logger.error(f'Error when switching alert pop')
            self.logger.exception(e)
        else:
            return alert

    def alert_process(self, process, message=None):
        try:
            alert = self.switch_alert()
            if(process == 'accept'):
                alert.accept()
            elif(process == 'dismiss'):
                alert.dismiss()
            elif(process == 'message'):
                alert.send_keys(message)
        except Exception as e:
            self.logger.error(f'Error when process alert')
            self.logger.exception(e) 
              
    def double_click(self, locator):
        WebDriverWait(self.driver, TestData.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        ).double_click(self, locator)

    def switch_alert(self):
        try:
            alert = self.driver.switch_to.alert
        except Exception as e:
            self.logger.error(f"Error when switching alert pop")
            self.logger.exception(e)
        else:
            return alert
            
               def alert_process(self, process, message=None):
        try:
            alert = self.switch_alert()
            if process == "accept":
                alert.accept()
            elif process == "dismiss":
                alert.dismiss()
            elif process == "message":
                alert.send_keys(message)
        except Exception as e:
            self.logger.error(f"Error when process alert")
            self.logger.exception(e)
            
            

import os, sys
sys.path.append(os.getcwd())
import logging
from config.configuration import Global

class Logger(logging.Logger):
    def __init__(self, logger, logger_level = logging.DEBUG) -> None:
        super().__init__(logger)
        formatter = logging.Formatter('[%(asctime)s] %(name)s - %(funcName)s - %(levelname)s - %(message)s')
        file_name = Global.LOG_DIR + Global.DATETIME_NOW + '_log.log'
        file_handler = logging.FileHandler(file_name, encoding="utf-8-sig")
        file_handler.setLevel(logger_level)
        file_handler.setFormatter(formatter)
        self.addHandler(file_handler)
        
        
        import inspect
import logging


def customLogger(loglevel=logging.DEBUG):
    #get the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    #By default , log all message
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                    datefmt="%m/%d/%Y %I:%M:%S %p")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
    
    
import logging
import time


class Logger():

    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        curr_time = time.strftime("%Y-%m-%d")
        self.LogFileName = '/Users/animeshmukherjee/PycharmProjects/pythonProject/Appium_Page_Object_Model/Logs/log' + curr_time + '.txt'
        # "a" to append the logs in same file, "w" to generate new logs and delete old one
        fh = logging.FileHandler(self.LogFileName, mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
        
        import os, sys
sys.path.append(os.getcwd())
import logging
from config.configuration import Global

class Logger(logging.Logger):
    def __init__(self, logger, logger_level = logging.DEBUG) -> None:
        super().__init__(logger)
        formatter = logging.Formatter('[%(asctime)s] %(name)s - %(funcName)s - %(levelname)s - %(message)s')
        file_name = Global.LOG_DIR + Global.DATETIME_NOW + '_log.log'
        file_handler = logging.FileHandler(file_name, encoding="utf-8-sig")
        file_handler.setLevel(logger_level)
        file_handler.setFormatter(formatter)
        self.addHandler(file_handler)
"""
