from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as Firefox_Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import pytest
import logging


def pytest_configure(config):
    # Set up basic configuration for your logs
    logging.basicConfig(
        level=logging.DEBUG,
        filename="test_logs.log",
        filemode="w",
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    # Increase log level for external libraries
    logging.getLogger("selenium").setLevel(logging.ERROR)
    logging.getLogger("webdriver_manager").setLevel(logging.ERROR)
    logging.getLogger("urllib3").setLevel(logging.ERROR)


def pytest_addoption(parser):
    """
    Adds command-line options
    """
    try:
        parser.addoption(
            "--browser",
            action="store",
            default="chrome",
            choices=("chrome", "firefox", "headless"),
            help="Choose browser, chrome(default) OR firefox",
        )
        parser.addoption(
            "--env",
            action="store",
            default="local",
            choices=("remote",),
            help="Choose the environment that you want to run the test, local OR remote",
        )

    except ValueError as e:
        print(e)


@pytest.fixture
def cmdopt(request):
    """
    Retrieve the value of a command line option
    """
    browser = request.config.getoption("--browser")
    return browser


@pytest.fixture
def init_driver(request):
    global driver
    try:
        browser = request.config.getoption("--browser").strip().lower()
        print("\n", "-" * 6, browser, "-" * 6)
        if browser == "chrome":
            options = Chrome_Options()
            driver = webdriver.Chrome(
                service=Service(executable_path=ChromeDriverManager().install()),
                options=options,
            )
        elif browser == "firefox":
            options = Firefox_Options()
            driver = webdriver.Firefox(
                service=Service(executable_path=GeckoDriverManager().install()),
                options=options,
            )
        elif browser == "headless":
            options = Firefox_Options()
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--headless")
            driver = webdriver.Firefox(
                service=Service(executable_path=GeckoDriverManager().install()),
                options=options,
            )

        print(f"before yield {driver =}")
        yield driver
        print(f"{driver =}")
        print(f"------ Tear Down {browser} ------")
        driver.quit()
        print("**** Test Completed ****")

    except Exception:
        import traceback

        traceback.print_exc()
        raise
