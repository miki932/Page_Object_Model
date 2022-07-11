from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options
import pytest
import os


@pytest.fixture(params=["chrome", "firefox"], scope="session")
def init_driver(request):
    global driver

    if request.param == "chrome":
        print("-" * 6, request.param, "-" * 6)
        options = Chrome_Options()
        options.headless = True
        driver = webdriver.Chrome(
            service=Service(
                executable_path=ChromeDriverManager().install()), options=options)
        request.driver = driver

    elif request.param == "firefox":
        print("-" * 6, request.param, "-" * 6)
        options = Firefox_Options()
        options.headless = True
        driver = webdriver.Firefox(
            service=Service(
            executable_path=GeckoDriverManager().install()), options=options)
        request.driver = driver

    yield driver
    print(f"------Tear Down {request.param}------")
    driver.close()


#Add a screenshot to report when a test failed
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url(driver.current_url))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::", "_") + ".png"
            destination_file = os.path.join(report_directory, file_name)
            driver.save_screenshot(destination_file)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px"' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                # only add additional html on failure
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


# fixture to automatically open the generated HTML Report in a browser.
@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    config._htmlfile = config._html.logfile


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session):
    file = session.config._htmlfile
    os.system('open ' + file)


# Read parameters from pytest Command Line
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Default browser")


"""
    # If we want to run our test on Selenium Grid via some cloud service:
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

"""
