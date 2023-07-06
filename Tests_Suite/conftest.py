from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options
import pytest
import subprocess


def pytest_addoption(parser):
    """
    ADD parameters to pytest Command Line
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
            help="Choose environment that you want run the test, local OR remote",
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

        elif browser == "headless":
            options = Chrome_Options()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
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
        print(f"before yield {driver =}")
        yield driver
        print(f"{driver =}")
        print(f"------ Tear Down {browser} ------")
        driver.quit()
        print("**** Test Completed ****")

    except Exception as e:
        print(e)
        raise


def pytest_sessionfinish(session, exitstatus):
    # Retrieve the Allure report directory path from pytest.ini
    allure_report_dir = session.config.getoption("--alluredir")

    # Open the Allure report using the Allure command-line tool
    subprocess.run(["allure", "serve", allure_report_dir], check=False)
