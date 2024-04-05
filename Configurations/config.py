import os

# You should insert here your private credentials,
# Notice: Do not upload secret information to GitHub ! Be careful !
BASE_URL = "https://www.saucedemo.com/"
HOME_PAGE_URL = "https://www.saucedemo.com/inventory.html"
CART_PAGE_URL = "https://www.saucedemo.com/cart.html"
USER_NAME = "standard_user"
INVALID_USER_NAME = "bad_user"
PASSWORD = "secret_sauce"
INVALID_PASSWORD = "12345"
TIMEOUT = 10
TITLE = "Swag Labs"

# Sauce Labs configuration:
SAUCE_USERNAME = ""
SAUCE_ACCESS_KEY = ""
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
