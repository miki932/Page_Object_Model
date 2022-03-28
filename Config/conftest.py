from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.params == "chrome":
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if request.params == "firefox":
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    request.cls.driver = web_driver
    yield
    web_driver.close()
