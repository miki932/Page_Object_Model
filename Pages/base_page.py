from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configurations.config import TestData
import pytest


@pytest.mark.usefixtures("init_driver")
class BasePage:
    """
    The Base_Page class is a parent of all pages
    that holds all common functionality across the website.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, TestData.TIMEOUT)

    def get_element(self, *locator):
        self.wait.until(EC.visibility_of_element_located(*locator))
        element = self.driver.find_element(*locator)
        return element.text

    def click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(*locator)).click()

    def send_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def hover(self, *locator):
        element = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def execute_javascript(self, js_script):
        """
        Execute JavaScript
        :param: Javascript to be executed
        :return: None / depends on Script
        """
        try:
            self.driver.execute_script(js_script)
        except Exception as e:
            print(e)

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        try:
            self.wait.until(EC.title_is(title))
        except TimeoutException:
            print("ERROR: ELEMENT NOT FOUND WITHIN GIVEN TIME")
        return self.driver.title

    def is_visible(self, *locator) -> bool:
        element = self.wait.until(EC.visibility_of_element_located(*locator))
        return bool(element)

    def get_url(self) -> str:
        return self.driver.current_url

    def get_element_attr(self):
        pass

    def is_link_work(self, url):
        url_exists = self.wait.until(EC.url_to_be(url))
        return url_exists

    def switch_tab(self):
        """
        I`m Not using this function anymore,
        Because the function `switch_window` (below) is a better approach from my point of view,
        Because I can handle whatever specific window I want (index), but both are ok and work well.
        """
        original_window = self.driver.current_window_handle
        self.wait.until(EC.number_of_windows_to_be(2))

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

    def is_disappeared(self, *locator, timeout=TestData.TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout, 1, TestData.TIMEOUT).until_not(
                EC.presence_of_element_located(*locator)
            )
        except TimeoutException:
            return False
        return True


"""

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
        
        
    # TODO: custom logger.
    # TODO: get element func.
    # TODO: TestPlan management integration.
    # TODO: Wrap all in Docker.
    # TODO: Run test in parallel.
    # TODO: Allure integration.
    # TODO: Pytest - Separate to regression/sanity etc.

"""
