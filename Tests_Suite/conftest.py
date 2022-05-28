from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options
import pytest
import os


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    global driver

    if request.param == "chrome":
        print("-" * 6, request.param, "-" * 6)
        options = Chrome_Options()
        options.headless = True
        driver = webdriver.Chrome(
            service=Service(executable_path=ChromeDriverManager().install()), options=options)
        request.cls.driver = driver

    elif request.param == "firefox":
        print("-" * 6, request.param, "-" * 6)
        options = Firefox_Options()
        options.headless = True
        driver = webdriver.Firefox(
            service=Service(executable_path=GeckoDriverManager().install()), options=options)
        request.cls.driver = driver

    yield driver
    print(f"------Tear Down {request.param}------")
    driver.close()


# fixture to automatically open the generated HTML Report in a browser.
@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    config._htmlfile = config._html.logfile


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session):
    file = session.config._htmlfile
    os.system('open ' + file)
    # invoke the file opening in external tool


    #If we want to run our test on Selenium Grid via some cloud service:
    # sauce_username = os.environ["SAUCE_USERNAME"]
    # sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
    # remote_url = f"http://{sauce_username}:{sauce_access_key}@ondemand.saucelabs.com/wd/hub"
    # sauce_options = {
    #     "screenResolution": "1280x768",
    #     "platformName": "Windows 10",
    #     "browserVersion": "61.0",
    #     "seleniumVersion": "3.11.0",
    #     'name': 'Pytest Chrome W3C Sample'
    # }
    #
    # chrome_opts =  {
    #     'platformName':"Windows 10",
    #     'browserName': "chrome",
    #     'browserVersion': '61.0',
    #     'goog:chromeOptions': {'w3c': True},
    #     'sauce:options': sauce_options
    # }
    #
    # driver = webdriver.Remote(remote_url, desired_capabilities=chrome_opts)
