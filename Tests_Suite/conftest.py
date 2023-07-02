from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options
import allure
import pytest
import os
import subprocess


def pytest_addoption(parser):
    """
    ADD parameters to pytest Command Line
    """
    try:
        parser.addoption(
            "--browser",
            action="store",
            default="chrome",
            choices=("chrome", "firefox", "headless"),
            help="Choose browser, chrome(default) OR firefox",
        )

        parser.addoption(
            "--env",
            action="store",
            default="local",
            choices=("remote",),
            help="Choose environment that you want run the test, local OR remote",
        )

    except ValueError as e:
        print(e)


@pytest.fixture
def cmdopt(request):
    """
    Retrieve the value of a command line option
    """
    browser = request.config.getoption("--browser")
    return browser


@pytest.fixture
def init_driver(request):
    global driver
    try:
        browser = request.config.getoption("--browser").strip().lower()
        print("-" * 6, browser, "-" * 6)
        if browser == "chrome":
            options = Chrome_Options()
            driver = webdriver.Chrome(
                service=Service(executable_path=ChromeDriverManager().install()),
                options=options,
            )

        elif browser == "headless":
            options = Chrome_Options()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            driver = webdriver.Chrome(
                service=Service(executable_path=ChromeDriverManager().install()),
                options=options,
            )

        elif browser == "firefox":
            options = Firefox_Options()
            driver = webdriver.Firefox(
                service=Service(executable_path=GeckoDriverManager().install()),
                options=options,
            )

        yield driver
        print(f"------Tear Down {browser}------")
        driver.quit()
        print("**** Test Completed ****")

    except Exception as e:
        print(e)


def pytest_sessionfinish(exitstatus, session):
    if exitstatus == pytest.ExitCode.TESTS_FAILED:
        return

    # Specify the path to the Allure report directory
    report_dir = "/Users/mtsioni/PycharmProjects/Page_Object_Model/Reports"

    # Open the Allure report in the web browser
    subprocess.run(["allure", "serve", report_dir], check=False)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        try:
            with open("failures", mode) as file:
                if "driver" in item.fixturenames:
                    web_driver = item.funcargs["driver"]
                    # Take a screenshot using the WebDriver and save it
                    screenshot = web_driver.get_screenshot_as_png()
                    file.write("Failure details:\n")
                    # Write additional failure information to the file
                    file.write(str(rep.longrepr))
                    allure.attach(
                        screenshot,
                        name="screenshot",
                        attachment_type=allure.attachment_type.PNG,
                    )
                else:
                    file.write(
                        "Failed to take a screenshot. No 'driver' fixture found.\n"
                    )
        except Exception as e:
            print(f"Failed to take a screenshot: {e}")


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
