import os
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium import webdriver
import pytest
import logging
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_configure(config):
    logging.basicConfig(
        level=logging.DEBUG,
        filename="test_logs.log",
        filemode="w",
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logging.getLogger("selenium").setLevel(logging.ERROR)
    logging.getLogger("webdriver_manager").setLevel(logging.ERROR)
    logging.getLogger("urllib3").setLevel(logging.ERROR)


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=os.getenv("BROWSER", "firefox"),
        choices=("chrome", "firefox", "headless"),
        help="Choose browser, chrome OR firefox",
    )
    parser.addoption(
        "--env",
        action="store",
        default=os.getenv("ENV", "local"),
        choices=("local", "grid"),
        help="Choose the environment that you want to run the test, local OR grid",
    )


@pytest.fixture
def cmdopt(request):
    browser = request.config.getoption("--browser")
    environment = request.config.getoption("--env")
    return browser, environment


@pytest.fixture
def init_driver(request):
    global driver
    try:
        browser, environment = (
            request.config.getoption("--browser").strip().lower(),
            request.config.getoption("--env").strip().lower(),
        )

        if environment == "local":
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
        elif environment == "grid":
            grid_url = f"http://{os.getenv('HUB_HOST', 'localhost')}:4444/wd/hub"

            if browser == "chrome":
                options = Chrome_Options()
                driver = webdriver.Remote(command_executor=grid_url, options=options)
            elif browser == "firefox":
                options = Firefox_Options()
                driver = webdriver.Remote(command_executor=grid_url, options=options)
            elif browser == "headless":
                options = Firefox_Options()
                options.add_argument("--disable-gpu")
                options.add_argument("--no-sandbox")
                options.add_argument("--headless")
                driver = webdriver.Remote(command_executor=grid_url, options=options)

        yield driver
        driver.quit()
    except Exception:
        import traceback

        traceback.print_exc()
        raise
