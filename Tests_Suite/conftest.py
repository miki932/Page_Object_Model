from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(params=["chrome", "firefox"], scope="session")
def init_driver(request):
    #options = Options()
    #options.add_argument("--headless")
    global driver
    print("------Setup driver------")
    if request.param == "chrome":
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))#add here chrome_options=options
        request.cls.driver = driver
    if request.param == "firefox":
        driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
        request.cls.driver = driver
    yield
    print("------Tear Down------")
    driver.close()
