import os
import datetime


class TestData:
    # You should insert here your credentials,
    # Notice: do not upload secret information to GitHub ! Be careful !
    SAUCE_USERNAME = ""
    SAUCE_ACCESS_KEY = ""

    BASE_URL = "https://www.saucedemo.com/"
    HOME_PAGE_URL = "https://www.saucedemo.com/inventory.html"
    USER_NAME = "standard_user"
    INVALID_USER_NAME = "bad_user"
    PASSWORD = "secret_sauce"
    INVALID_PASSWORD = "12345"
    TIMEOUT = 10
    TITLE = "Swag Labs"

    TEST_TITLE = ""
    PROJECT_ROOT_DIR = file_path = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
    LOG_DIR = PROJECT_ROOT_DIR + "/logs/"
    REPORT_DIR = PROJECT_ROOT_DIR + "/reports/"
    DATA_DIR = PROJECT_ROOT_DIR + "/data/"
    IMAGE_DIR = REPORT_DIR + "/images/"
    BROWSER = "chrome"
    DATETIME_NOW = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
