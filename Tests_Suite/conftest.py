from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options
import pytest


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    options = chrome_options()
    options.headless = True
    global driver
    print("------Setup driver------")
    if request.param == "chrome":
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)
        request.cls.driver = driver
        print("------Chrome driver------")
    options = firefox_options()
    options.headless = True
    if request.param == "firefox":
        driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()), options=options)
        request.cls.driver = driver
    yield driver
    print("------Tear Down------")
    driver.close()
