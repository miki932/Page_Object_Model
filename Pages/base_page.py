import pytest
from selenium.common import TimeoutException, JavascriptException, NoSuchWindowException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configurations import config
import logging


logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("init_driver")
class BasePage:
    """
    The Base_Page class is a parent of all pages
    that holds all common functionality across the website.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, config.TIMEOUT)

    def get_element(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        """
        TODO: verify if this func working as expected
        """
        return self.wait.until(EC.visibility_of_element_located(locator)).get_attribute(
            "innerText"
        )

    def hover(self, *locator):
        element = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def execute_javascript(self, js_script):
        """Executes JavaScript in the current window/frame."""
        try:
            self.driver.execute_script(js_script)
        except JavascriptException:
            logger.exception("Failed to execute JavaScript.")
            raise

    def get_title(self, title: str) -> str:
        """Returns the title of the page"""
        try:
            self.wait.until(EC.title_is(title))
            return self.driver.title
        except TimeoutException:
            logger.error("ERROR: ELEMENT NOT FOUND WITHIN GIVEN TIME")

    def is_visible(self, locator) -> bool:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return bool(element)

    def get_url(self) -> str:
        return self.driver.current_url

    def is_link_work(self, url):
        url_exists = self.wait.until(EC.url_to_be(url))
        return url_exists

    def get_current_window_handle(self):
        return self.driver.current_window_handle

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

    def switch_window(self, index: int):
        try:
            self.driver.switch_to.window(self.driver.window_handles[index])
        except IndexError as index_error:
            logger.error(index_error)
        except NoSuchWindowException as no_such_window_exception:
            logger.error(no_such_window_exception)
        except Exception as e:
            logger.error(e)

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

    def dismiss_alert(self, text=""):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        if text in alert_text:
            alert.dismiss()
        else:
            raise Exception(
                f"Invalid alert with text {alert_text} and not containing {text}"
            )

    def focus(self):
        another_window = list(
            set(self.driver.window_handles) - {self.driver.current_window_handle}
        )[0]
        self.driver.switch_to.window(another_window)

    def is_disappeared(self, locator, timeout=config.TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            return False
        return True


"""
    # TODO: get element func.
    # TODO: Wrap all in Docker.
    # TODO: Run test in parallel.
    # TODO: Pytest - Separate to regression/sanity etc.
"""
