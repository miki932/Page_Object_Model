from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(params=["chrome", "firefox"], scope="session")
def init_driver(request):
    options = Options()
    options.add_argument("--headless")
    if request.params == "chrome":
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()),chrome_options=options)
    if request.params == "firefox":
        driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    request.cls.driver = driver
    yield
    driver.close()
