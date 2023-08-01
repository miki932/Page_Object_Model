from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as Firefox_Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv
from selenium import webdriver
import pytest
import qaseio
import os
import datetime
from qaseio.model.run_create import RunCreate
from Configurations.config import URL_API

# Load the environment variables from the ".env" file
load_dotenv()


@pytest.fixture(scope="session")
def qase_client():
    """Creates a Qase.io client object."""
    qase_token = os.getenv("QASE_API_TOKEN")

    # Create a Configuration object
    configuration = qaseio.Configuration(api_key=qase_token, host=URL_API)

    # Set the API key
    # configuration.api_key = qase_token

    # Disable SSL verification for Qase.io API requests
    configuration.verify_ssl = False

    # Pass the configuration object to the ApiClient
    qase_client = qaseio.ApiClient(configuration=configuration)
    yield qase_client


@pytest.fixture(scope="session", autouse=True)
def create_test_run(request, qase_client):
    # Project code
    qase_project_code = os.getenv("QASE_PROJECT_CODE")

    # Initialize the RunsApi using the qase_client
    runs_api = qaseio.RunsApi(qase_client)

    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_name = f"Test_run : {current_time}"

    # Delete existing test run (if any)
    # existing_runs = runs_api.get_runs(code=qase_project_code)
    # for existing_run in existing_runs:
    #     runs_api.delete_run(code=qase_project_code, id=existing_run.id)

    # Create a new test run with the desired title
    run_class = RunCreate(title=run_name)
    new_run = runs_api.create_run(code=qase_project_code, run_create=run_class)
    run_id = new_run.id
    setattr(
        request.session, "qase_run_id", run_id
    )  # Store the run_id in the test session

    yield

    # Complete the test run after running all the tests
    run_id = getattr(request.session, "qase_run_id", None)
    if run_id:
        try:
            runs_api.complete_run(code=qase_project_code, id=run_id)
        except Exception as e:
            print(f"Error completing test run: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    run_id = getattr(
        item, "qase_run_id", None
    )  # Access the run_id stored in the test item

    if run_id:
        qase_test_case_id = item.function.qase.args[
            0
        ]  # Get the test case ID from the marker
        status = "passed" if rep.passed else "failed"

        # Report the test result to the test run
        qase_client.results.create_result(qase_test_case_id, run_id, {"status": status})


@pytest.fixture(scope="function", autouse=True)
def complete_test_run(request, qase_client):
    run_id = getattr(request.node.cls, "qase_run_id", None)

    yield

    # Complete the test run after running all the tests
    if run_id:
        qase_client.runs.complete_run(run_id)


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
        parser.addoption(
            "--qase",
            action="store_true",
            default=False,
            help="Enable Qase.io integration",
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
        print("\n", "-" * 6, browser, "-" * 6)
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
        print(f"before yield {driver =}")
        yield driver
        print(f"{driver =}")
        print(f"------ Tear Down {browser} ------")
        driver.quit()
        print("**** Test Completed ****")

    except Exception:
        import traceback

        traceback.print_exc()
        raise


"""
# Load the environment variables from .env file
load_dotenv()


@pytest.fixture(scope="session")
def qase_run(qase_testrun):
    #Create a test run in Qase Test Management
    api_token = os.getenv("QASE_API_TOKEN")
    project_code = os.getenv("QASE_PROJECT_CODE")

    timestamp = datetime.now().strftime("%Y%m%d%H%M")
    title = f"Test_Run_{qase_testrun.run_id}:{timestamp}"
    qase_testrun.create_run(title=title, description="Testing with Qase",
                            api_token=api_token, project_code=project_code)
    statuses = {}

    yield statuses

    # Report test case statuses at the end
    for testcase_id, status in statuses.items():
        qase_testrun.report_status(testcase_id, status)

    # Complete the test run
    qase_testrun.complete_run()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_protocol(item, nextitem):
    #Collects the status of each test case
    qase_run = item.session.qase_run
    qase_testrun = item.session.qase_testrun

    if hasattr(item, "get_closest_marker"):
        qase_marker = item.get_closest_marker("qase")
        if qase_marker is not None:
            testcase_id = qase_marker.args[0]
            status = "passed" if item.passed else "failed"
            qase_run[testcase_id] = status
            qase_testrun.report_status(testcase_id, status)

    return None







@pytest.fixture(scope="function")
def report_results(test_run):
    #Report the results of the test to the test run.
    for test_case in pytest.current_test_session.tests:
        status = "PASSED" if test_case.passed else "FAILED"
        qaseio.report_test_case_result(test_run.id, test_case.nodeid, status)

def pytest_sessionfinish(session, exitstatus):
    #Report the results of the test run to Qase.
    status = "PASSED" if exitstatus == 0 else "FAILED"
    qaseio.report_test_run_status(test_run.id, status)

def pytest_runtest_protocol(item, nextitem):
    test_run_id = item.config.cache.get("test_run_id", default=None)
    if test_run_id:
        # Retrieve the Qase test case ID from the marker
        qase_marker = item.get_closest_marker("qase")
        if qase_marker:
            qase_case_id = qase_marker.args[0]
            # Assign the Qase test case ID to the test case
            item.qase_case_id = qase_case_id
    return None


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    test_run_id = config.cache.get("test_run_id", default=None)
    if test_run_id:
        terminalreporter.write_line("Test run completed successfully.")
    else:
        terminalreporter.write_line("Test run completed with errors.")


@pytest.fixture(scope="function", autouse=True)
def report_test_result(request):
    #Report test cases to Qase.io

    # This fixture is executed for each test case automatically
    yield

    # After each test case, report the test result to Qase
    qase_case_id = getattr(request.node, "qase_case_id", None)
    if qase_case_id:
        try:
            outcome = request.node.result
            status = "passed" if outcome.outcome == "passed" else "failed"
        except AttributeError:
            # If the outcome attribute is not available, assume the test failed
            status = "failed"

        # Get the test run ID from the cache
        test_run_id = request.config.cache.get("test_run_id", default=None)

        # Report the test case result to Qase
        add_test_case_result(test_run_id, qase_case_id, status)


@pytest.fixture(scope="session")
def test_run_id(request):
    #Fixture to create the test run and return its ID
    title_prefix = "Test Run"
    description = "This is a test run"
    run_id = create_test_run(title_prefix, description)
    request.config.cache.set("test_run_id", run_id)
    return run_id
    

def pytest_sessionfinish(session, exitstatus):
    #Open the Allure Report automatically 

    # Retrieve the Allure report, the directory path from pytest.ini
    allure_report_dir = session.config.getoption("--alluredir")

    # Open the Allure report using the Allure command-line tool
    subprocess.run(["allure", "serve", allure_report_dir], check=False)

    # Complete the test run in Qase
    test_run_id = session.config.cache.get("test_run_id")
    if test_run_id:
        complete_test_run(test_run_id)
        print("Test run completed successfully.")
        
        
def pytest_runtest_protocol(item, nextitem):
    # This hook is executed before and after each test case

    # Perform actions before each test case
    print(f"Running test case: {item.nodeid}")

    # Run the test case
    try:
        item.runtest()
    except AssertionError as e:
        # Handle assertion errors
        print("Assertion error occurred:", e)
    except Exception as e:
        # Handle other unexpected exceptions
        print("Unexpected exception occurred:")
        traceback.print_exc()

    # Perform actions after each test case
    if nextitem is None:
        # After the last test case, perform any necessary actions
        print("All test cases executed!")


def pytest_runtest_makereport(item, call, report):
    # Perform actions before each test case
    print(f"Running test case: {item.nodeid}")

    # Check the outcome of the test case
    if report.failed:
        # Handle failed test case
        print("Test case failed:", report.longrepr)
    elif report.skipped:
        # Handle skipped test case
        print("Test case skipped:", report.longrepr)
    elif report.passed:
        # Handle passed test case
        print("Test case passed!")

    # Perform actions after each test case
    if report.when == "call" and report.passed:
        # After each test case, perform any necessary actions
        print("Actions after test case execution")

    # Return the report
    return report
"""
