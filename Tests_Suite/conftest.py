from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from dotenv import load_dotenv
import pytest
import os


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    options = Chrome_Options()
    options.headless = True
    global driver
    print("------Setup driver------")
    """
    #If we want to run our test on Selenium Grid via some cloud service:
    sauce_username = os.environ["SAUCE_USERNAME"]
    sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
    remote_url = f"http://{sauce_username}:{sauce_access_key}@ondemand.saucelabs.com/wd/hub"
    sauceOptions = {
        "screenResolution": "1280x768",
        "platformName": "Windows 10",
        "browserVersion": "61.0",
        "seleniumVersion": "3.11.0",
        'name': 'Pytest Chrome W3C Sample'
    }

    chromeOpts =  {
        'platformName':"Windows 10",
        'browserName': "chrome",
        'browserVersion': '61.0',
        'goog:chromeOptions': {'w3c': True},
        'sauce:options': sauceOptions
    }
    
    driver = webdriver.Remote(remote_url, desired_capabilities=chromeOpts)
    """
    if request.param == "chrome":
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)
        request.cls.driver = driver
        print("------Chrome driver------")
    options = Firefox_Options()
    options.headless = True
    if request.param == "firefox":
        driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()), options=options)
        request.cls.driver = driver
    yield driver
    print("------Tear Down------")
    driver.close()

# fixture to automatically open the generated HTML Report in a browser.
@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    config._htmlfile = config._html.logfile

@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session):
    file = session.config._htmlfile
    # invoke the file opening in external tool
    os.system('open ' + file)
