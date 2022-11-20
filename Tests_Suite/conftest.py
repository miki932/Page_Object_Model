import allure
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
    print(driver)
    try:
        if request.param == "chrome":
            print("-" * 6, request.param, "-" * 6)
            options = Chrome_Options()
            options.headless = True
            options.add_argument("--disable-gpu")
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        try:
            with open("failures", mode):
                if "driver" in item.fixturenames:
                    web_driver = item.funcargs["driver"]
                else:
                    print("Fail to take screen-shot")
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            print(f"Fail to take screen-shot: {e}")


def pytest_addoption(parser):
    """
    Read parameters from pytest Command Line
    Parse the input variables from the cli
    """
    try:
        parser.addoption(
            "--browser", action="store", default="firefox", help="Default browser"
        )
    except ValueError as e:
        print(e)


"""
@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    # fixture to automatically open the generated HTML Report in a browser.

    config._htmlfile = config._html.logfile


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session):
    file = session.config._htmlfile
    os.system("open " + file)
    
    
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    #Add a screenshot to report when a test failed
    
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
"""
