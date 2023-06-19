import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configurations import config


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
        return element.text

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
        try:
            self.driver.execute_script(js_script)
        except Exception as e:
            print("Error executing JavaScript:", e)

    def get_title(self, title) -> str:
        """Returns the title of the page"""
        try:
            self.wait.until(EC.title_is(title))
        except TimeoutException:
            print("ERROR: ELEMENT NOT FOUND WITHIN GIVEN TIME")
        return self.driver.title

    def is_visible(self, locator) -> bool:
        element = self.wait.until(EC.visibility_of_element_located(locator))
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
    # TODO: custom logger.
    # TODO: get element func.
    # TODO: TestPlan management integration.
    # TODO: Wrap all in Docker.
    # TODO: Run test in parallel.
    # TODO: Allure integration.
    # TODO: Pytest - Separate to regression/sanity etc.
"""
