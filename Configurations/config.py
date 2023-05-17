import os


# You should insert here your private credentials,
# Notice: Do not upload secret information to GitHub ! Be careful !

BASE_URL = "https://www.saucedemo.com/"
HOME_PAGE_URL = "https://www.saucedemo.com/inventory.html"
USER_NAME = "standard_user"
INVALID_USER_NAME = "bad_user"
PASSWORD = "secret_sauce"
INVALID_PASSWORD = "12345"
TIMEOUT = 10
TITLE = "Swag Labs"

# Sauce Labs configuration:
SAUCE_USERNAME = ""
SAUCE_ACCESS_KEY = ""

# Qase configuration:
QASE_API = "https://api.qase.io/v1"
QASE_TOKEN = ""
RUN_ID = ""
# TEST_TITLE = ""
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# LOG_DIR = PROJECT_ROOT_DIR + "/logs/"
# REPORT_DIR = PROJECT_ROOT_DIR + "/reports/"
# DATA_DIR = PROJECT_ROOT_DIR + "/data/"
# IMAGE_DIR = REPORT_DIR + "/images/"
# DATETIME_NOW = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
