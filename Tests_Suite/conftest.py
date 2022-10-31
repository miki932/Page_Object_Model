from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options
import pytest
import os

driver = None


@pytest.fixture(params=["chrome"], scope="session")
def init_driver(request):
    global driver
    """
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
    """
    try:
        if request.param == "chrome":
            print("-" * 6, request.param, "-" * 6)
            options = Chrome_Options()
            # options.headless = True
            driver = webdriver.Chrome(
                service=Service(executable_path=ChromeDriverManager().install()),
                options=options,
            )
            request.driver = driver

        elif request.param == "firefox":
            print("-" * 6, request.param, "-" * 6)
            options = Firefox_Options()
            # options.headless = True
            driver = webdriver.Firefox(
                service=Service(executable_path=GeckoDriverManager().install()),
                options=options,
            )
            request.driver = driver

        yield driver
        print(f"------Tear Down {request.param}------")
        driver.quit()
        print("**** Test Completed ****")
    except Exception as e:
        print(e)


# Add a screenshot to report when a test failed
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
                html = (
                    '<div><img src="%s" alt="screenshot" style="width:300px;height=200px"'
                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
                )
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
    os.system("open " + str(file))


# Read parameters from pytest Command Line
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Default browser"
    )
