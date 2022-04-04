from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    if request.params == "chrome":
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
    if request.params == "firefox":
        driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    request.cls.driver = driver
    yield
    driver.close()
